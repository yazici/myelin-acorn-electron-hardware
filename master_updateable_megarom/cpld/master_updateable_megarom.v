// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.


module master_updateable_megarom(
  inout wire [7:0] D,
  input wire [16:0] bbc_A,
  output wire [18:0] flash_A,
  output wire flash_nOE,
  output wire flash_nWE,
  input wire cpld_SCK,
  input wire cpld_MOSI,
  input wire cpld_SS,
  output reg cpld_MISO,
  input wire [1:0] cpld_JP
);

// flash bank to use for BBC reads
reg [1:0] flash_bank = 2'b0;

// address value from SPI transaction
reg [18:0] spi_A = 19'b0;

// data value from SPI transaction
reg [7:0] spi_D = 8'b0;

// 1 to pass the bbc_A through to flash_A, 0 to use A instead
reg allowing_bbc_access_int = 1'b1;
wire allowing_bbc_access;

// 1 to drive flash_nOE or flash_nWR
reg reading_memory = 1'b0;
reg writing_memory = 1'b0;

// 1 for read (drive flash_nOE), 0 for write (drive flash_nWR)
reg rnw = 1'b0;

// 1 to pass spi_D through to D
reg driving_bus = 1'b0;

// counts up to 50; need 6 bits
reg [5:0] spi_bit_count = 6'b000000;



// disallow bbc access during SPI transactions, and when we've set the sticky
// bit.
assign allowing_bbc_access = allowing_bbc_access_int && cpld_SS;

// We're either passing bbc_A through to flash_A, with D tristated, or we're
// controlling both and ignoring bbc_A.
assign flash_A = (allowing_bbc_access == 1'b1) ? {flash_bank, bbc_A} : spi_A;
// assert OE
assign flash_nOE = !(allowing_bbc_access || reading_memory);
// assert WE and D when the BBC is disabled and we're doing a memory write
assign flash_nWE = !(!allowing_bbc_access && writing_memory);
// drive D when writing
assign D = (allowing_bbc_access == 1'b0 && (driving_bus == 1'b1 && rnw == 1'b0)) ? spi_D : 8'bZZZZZZZZ;

always @(posedge cpld_SCK or posedge cpld_SS) begin

  if (cpld_SS == 1'b1) begin
    reading_memory <= 1'b0;
    writing_memory <= 1'b0;
    driving_bus <= 1'b0;
    spi_bit_count <= 6'b000000;
  end else begin
    // the master device should bring cpld_SS high between every transaction.

    // SPI is big-endian; send the MSB first and clock into the LSB.

    // to block out the BBC and enable flash access: send ffffff00. to reenable
    // the BBC, send 32 bits of ones.  the final bit sets 'allowing_bbc_access'.

    // message format for a WRITE that blocks the BBC after: 19 address bits,
    // rnw, 8 data bits, 4 zeros, with the write happening during the six zeros.

    // message format for a READ that blocks the BBC after: 19 address bits,
    // rnw, 12 zeros, with the data byte returned in the final 8 bits.

    // so if you want to do a single read and reenable BBC access afterward,
    // send 19 address bits, then 1000000000001.

    // the flash chip only needs a 40ns low pulse on /CE + /WE, and its read
    // access time is 55-70ns.  we hold /OE for reads or /WE for writes low for
    // three SCK periods, so for a 70ns flash chip, the SPI clock period must be
    // less than 42.8 MHz.

    if (spi_bit_count < 19) begin
      spi_A <= {spi_A[17:0], cpld_MOSI};
    end else if (spi_bit_count == 19) begin
      rnw <= cpld_MOSI;
    end else if (rnw == 1'b1) begin
      // 0-18 address, 19 rnw, 20-23 access, 24-31 data out
      if (spi_bit_count == 20) begin
        // start read
        reading_memory <= 1'b1;
      end else if (spi_bit_count == 23) begin
        // end read
        reading_memory <= 1'b0;
        spi_D <= D;
      end else if (spi_bit_count >= 24) begin
        spi_D <= {spi_D[6:0], 1'b0};
      end
    end else if (rnw == 1'b0) begin
      // 0-18 address, 19 rnw, 20-27 data in, 28-31 access
      if (spi_bit_count < 28) begin
        spi_D <= {spi_D[6:0], cpld_MOSI};
      end
      if (spi_bit_count == 27) begin
        driving_bus <= 1'b1;
      end
      if (spi_bit_count == 28) begin
        writing_memory <= 1'b1;
      end
      if (spi_bit_count == 30) begin
        writing_memory <= 1'b0;
      end
      if (spi_bit_count == 31) begin
        driving_bus <= 1'b0;
      end
    end
    if (spi_bit_count == 31) begin
      allowing_bbc_access_int <= cpld_MOSI;
    end
    spi_bit_count <= spi_bit_count + 1;
  end
end

always @(negedge cpld_SCK or posedge cpld_SS) begin
  if (cpld_SS == 1'b1) begin
    cpld_MISO <= 1'b0;
  end else if (spi_bit_count < 19) begin
    cpld_MISO <= spi_A[18]; // clock out last address
  end else begin
    cpld_MISO <= spi_D[7];
  end
end

endmodule
