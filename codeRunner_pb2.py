# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: codeRunner.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='codeRunner.proto',
  package='CodeRunner',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x63odeRunner.proto\x12\nCodeRunner\"_\n\x11\x63odeRunnerRequest\x12+\n\tlanguage_\x18\x01 \x01(\x0e\x32\x18.CodeRunner.codeLanguage\x12\r\n\x05\x63ode_\x18\x02 \x01(\t\x12\x0e\n\x06input_\x18\x03 \x01(\t\"K\n\x11\x63odeRunnerRespone\x12%\n\x05type_\x18\x01 \x01(\x0e\x32\x16.CodeRunner.resultType\x12\x0f\n\x07result_\x18\x02 \x01(\t*!\n\x0c\x63odeLanguage\x12\x07\n\x03\x43pp\x10\x00\x12\x08\n\x04Java\x10\x01*\x84\x01\n\nresultType\x12\n\n\x06Sucess\x10\x00\x12\x11\n\rCompile_Error\x10\x01\x12\x11\n\rRuntime_Error\x10\x02\x12\x17\n\x13Time_Limit_Exceeded\x10\x03\x12\x19\n\x15Memory_Limit_Exceeded\x10\x04\x12\x10\n\x0cSystem_Error\x10\x05\x32U\n\ncodeRunner\x12G\n\x05judge\x12\x1d.CodeRunner.codeRunnerRequest\x1a\x1d.CodeRunner.codeRunnerRespone\"\x00\x62\x06proto3'
)

_CODELANGUAGE = _descriptor.EnumDescriptor(
  name='codeLanguage',
  full_name='CodeRunner.codeLanguage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Cpp', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Java', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=206,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_CODELANGUAGE)

codeLanguage = enum_type_wrapper.EnumTypeWrapper(_CODELANGUAGE)
_RESULTTYPE = _descriptor.EnumDescriptor(
  name='resultType',
  full_name='CodeRunner.resultType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Sucess', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Compile_Error', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Runtime_Error', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Time_Limit_Exceeded', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Memory_Limit_Exceeded', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='System_Error', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=242,
  serialized_end=374,
)
_sym_db.RegisterEnumDescriptor(_RESULTTYPE)

resultType = enum_type_wrapper.EnumTypeWrapper(_RESULTTYPE)
Cpp = 0
Java = 1
Sucess = 0
Compile_Error = 1
Runtime_Error = 2
Time_Limit_Exceeded = 3
Memory_Limit_Exceeded = 4
System_Error = 5



_CODERUNNERREQUEST = _descriptor.Descriptor(
  name='codeRunnerRequest',
  full_name='CodeRunner.codeRunnerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_', full_name='CodeRunner.codeRunnerRequest.language_', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code_', full_name='CodeRunner.codeRunnerRequest.code_', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_', full_name='CodeRunner.codeRunnerRequest.input_', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=32,
  serialized_end=127,
)


_CODERUNNERRESPONE = _descriptor.Descriptor(
  name='codeRunnerRespone',
  full_name='CodeRunner.codeRunnerRespone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_', full_name='CodeRunner.codeRunnerRespone.type_', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_', full_name='CodeRunner.codeRunnerRespone.result_', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=129,
  serialized_end=204,
)

_CODERUNNERREQUEST.fields_by_name['language_'].enum_type = _CODELANGUAGE
_CODERUNNERRESPONE.fields_by_name['type_'].enum_type = _RESULTTYPE
DESCRIPTOR.message_types_by_name['codeRunnerRequest'] = _CODERUNNERREQUEST
DESCRIPTOR.message_types_by_name['codeRunnerRespone'] = _CODERUNNERRESPONE
DESCRIPTOR.enum_types_by_name['codeLanguage'] = _CODELANGUAGE
DESCRIPTOR.enum_types_by_name['resultType'] = _RESULTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

codeRunnerRequest = _reflection.GeneratedProtocolMessageType('codeRunnerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CODERUNNERREQUEST,
  '__module__' : 'codeRunner_pb2'
  # @@protoc_insertion_point(class_scope:CodeRunner.codeRunnerRequest)
  })
_sym_db.RegisterMessage(codeRunnerRequest)

codeRunnerRespone = _reflection.GeneratedProtocolMessageType('codeRunnerRespone', (_message.Message,), {
  'DESCRIPTOR' : _CODERUNNERRESPONE,
  '__module__' : 'codeRunner_pb2'
  # @@protoc_insertion_point(class_scope:CodeRunner.codeRunnerRespone)
  })
_sym_db.RegisterMessage(codeRunnerRespone)



_CODERUNNER = _descriptor.ServiceDescriptor(
  name='codeRunner',
  full_name='CodeRunner.codeRunner',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=376,
  serialized_end=461,
  methods=[
  _descriptor.MethodDescriptor(
    name='judge',
    full_name='CodeRunner.codeRunner.judge',
    index=0,
    containing_service=None,
    input_type=_CODERUNNERREQUEST,
    output_type=_CODERUNNERRESPONE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CODERUNNER)

DESCRIPTOR.services_by_name['codeRunner'] = _CODERUNNER

# @@protoc_insertion_point(module_scope)
