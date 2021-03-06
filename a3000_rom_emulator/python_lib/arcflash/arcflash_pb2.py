# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arcflash.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arcflash.proto',
  package='arcflash',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x61rcflash.proto\x12\x08\x61rcflash\"g\n\tFlashBank\x12\x10\n\x08\x62\x61nk_ptr\x18\x01 \x01(\x05\x12\x10\n\x08\x62\x61nk_tag\x18\x02 \x01(\t\x12\x11\n\tbank_size\x18\x03 \x01(\x05\x12\x11\n\tbank_name\x18\x04 \x01(\t\x12\x10\n\x08\x63mos_tag\x18\x05 \x01(\t\"o\n\x0f\x46lashDescriptor\x12!\n\x04\x62\x61nk\x18\x01 \x03(\x0b\x32\x13.arcflash.FlashBank\x12\x11\n\thash_sha1\x18\x02 \x01(\t\x12\x12\n\nflash_size\x18\x03 \x01(\x05\x12\x12\n\nfree_space\x18\x04 \x01(\x05\"O\n\x04\x43MOS\x12\x10\n\x08\x63mos_tag\x18\x01 \x01(\t\x12\x10\n\x08\x62\x61nk_ptr\x18\x02 \x01(\x05\x12\x10\n\x08\x62\x61nk_tag\x18\x03 \x01(\t\x12\x11\n\tcmos_data\x18\x04 \x01(\x0c\x62\x06proto3')
)




_FLASHBANK = _descriptor.Descriptor(
  name='FlashBank',
  full_name='arcflash.FlashBank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bank_ptr', full_name='arcflash.FlashBank.bank_ptr', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_tag', full_name='arcflash.FlashBank.bank_tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_size', full_name='arcflash.FlashBank.bank_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_name', full_name='arcflash.FlashBank.bank_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmos_tag', full_name='arcflash.FlashBank.cmos_tag', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=131,
)


_FLASHDESCRIPTOR = _descriptor.Descriptor(
  name='FlashDescriptor',
  full_name='arcflash.FlashDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bank', full_name='arcflash.FlashDescriptor.bank', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_sha1', full_name='arcflash.FlashDescriptor.hash_sha1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flash_size', full_name='arcflash.FlashDescriptor.flash_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_space', full_name='arcflash.FlashDescriptor.free_space', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=244,
)


_CMOS = _descriptor.Descriptor(
  name='CMOS',
  full_name='arcflash.CMOS',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cmos_tag', full_name='arcflash.CMOS.cmos_tag', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_ptr', full_name='arcflash.CMOS.bank_ptr', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bank_tag', full_name='arcflash.CMOS.bank_tag', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cmos_data', full_name='arcflash.CMOS.cmos_data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=325,
)

_FLASHDESCRIPTOR.fields_by_name['bank'].message_type = _FLASHBANK
DESCRIPTOR.message_types_by_name['FlashBank'] = _FLASHBANK
DESCRIPTOR.message_types_by_name['FlashDescriptor'] = _FLASHDESCRIPTOR
DESCRIPTOR.message_types_by_name['CMOS'] = _CMOS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FlashBank = _reflection.GeneratedProtocolMessageType('FlashBank', (_message.Message,), dict(
  DESCRIPTOR = _FLASHBANK,
  __module__ = 'arcflash_pb2'
  # @@protoc_insertion_point(class_scope:arcflash.FlashBank)
  ))
_sym_db.RegisterMessage(FlashBank)

FlashDescriptor = _reflection.GeneratedProtocolMessageType('FlashDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _FLASHDESCRIPTOR,
  __module__ = 'arcflash_pb2'
  # @@protoc_insertion_point(class_scope:arcflash.FlashDescriptor)
  ))
_sym_db.RegisterMessage(FlashDescriptor)

CMOS = _reflection.GeneratedProtocolMessageType('CMOS', (_message.Message,), dict(
  DESCRIPTOR = _CMOS,
  __module__ = 'arcflash_pb2'
  # @@protoc_insertion_point(class_scope:arcflash.CMOS)
  ))
_sym_db.RegisterMessage(CMOS)


# @@protoc_insertion_point(module_scope)
