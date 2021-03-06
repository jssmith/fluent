# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functions.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='functions.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x66unctions.proto\"&\n\x08\x46unction\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x62ody\x18\x02 \x02(\x0c\"4\n\x05Value\x12\x0c\n\x04\x62ody\x18\x01 \x02(\x0c\x12\x1d\n\x04type\x18\x02 \x01(\x0e\x32\x0f.SerializerType\"F\n\x0c\x46unctionCall\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x12\n\nrequest_id\x18\x02 \x02(\r\x12\x14\n\x04\x61rgs\x18\x03 \x03(\x0b\x32\x06.Value\"\x1d\n\x0c\x46unctionList\x12\r\n\x05names\x18\x01 \x03(\t*4\n\x0eSerializerType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06STRING\x10\x01\x12\t\n\x05NUMPY\x10\x02')
)

_SERIALIZERTYPE = _descriptor.EnumDescriptor(
  name='SerializerType',
  full_name='SerializerType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMPY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=216,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_SERIALIZERTYPE)

SerializerType = enum_type_wrapper.EnumTypeWrapper(_SERIALIZERTYPE)
DEFAULT = 0
STRING = 1
NUMPY = 2



_FUNCTION = _descriptor.Descriptor(
  name='Function',
  full_name='Function',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Function.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='Function.body', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=57,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='Value.body', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='Value.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=111,
)


_FUNCTIONCALL = _descriptor.Descriptor(
  name='FunctionCall',
  full_name='FunctionCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='FunctionCall.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='FunctionCall.request_id', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='FunctionCall.args', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=183,
)


_FUNCTIONLIST = _descriptor.Descriptor(
  name='FunctionList',
  full_name='FunctionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='names', full_name='FunctionList.names', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=214,
)

_VALUE.fields_by_name['type'].enum_type = _SERIALIZERTYPE
_FUNCTIONCALL.fields_by_name['args'].message_type = _VALUE
DESCRIPTOR.message_types_by_name['Function'] = _FUNCTION
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['FunctionCall'] = _FUNCTIONCALL
DESCRIPTOR.message_types_by_name['FunctionList'] = _FUNCTIONLIST
DESCRIPTOR.enum_types_by_name['SerializerType'] = _SERIALIZERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Function = _reflection.GeneratedProtocolMessageType('Function', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTION,
  __module__ = 'functions_pb2'
  # @@protoc_insertion_point(class_scope:Function)
  ))
_sym_db.RegisterMessage(Function)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'functions_pb2'
  # @@protoc_insertion_point(class_scope:Value)
  ))
_sym_db.RegisterMessage(Value)

FunctionCall = _reflection.GeneratedProtocolMessageType('FunctionCall', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCALL,
  __module__ = 'functions_pb2'
  # @@protoc_insertion_point(class_scope:FunctionCall)
  ))
_sym_db.RegisterMessage(FunctionCall)

FunctionList = _reflection.GeneratedProtocolMessageType('FunctionList', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONLIST,
  __module__ = 'functions_pb2'
  # @@protoc_insertion_point(class_scope:FunctionList)
  ))
_sym_db.RegisterMessage(FunctionList)


# @@protoc_insertion_point(module_scope)
