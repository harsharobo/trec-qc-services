# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sample_service.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14sample_service.proto\":\n\x0fQuestionDetails\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x15\n\rquestionClass\x18\x02 \x01(\t\"l\n\x12QuestionPOSTagging\x12)\n\x0fquestionDetails\x18\x01 \x01(\x0b\x32\x10.QuestionDetails\x12\x16\n\x0etaggedQuestion\x18\x02 \x01(\t\x12\x13\n\x0btagSequence\x18\x03 \x03(\t\"x\n\x13GetQuestionsMessage\x12\r\n\x05limit\x18\x01 \x01(\x05\x12-\n\x13questionDetailsList\x18\x02 \x03(\x0b\x32\x10.QuestionDetails\x12\x11\n\trequestId\x18\x03 \x01(\t\x12\x10\n\x08\x66romHost\x18\x04 \x01(\t2\xeb\x01\n\x1eQuestionClassificationServices\x12@\n\x12getSampleQuestions\x12\x14.GetQuestionsMessage\x1a\x14.GetQuestionsMessage\x12G\n\x15streamSampleQuestions\x12\x14.GetQuestionsMessage\x1a\x14.GetQuestionsMessage(\x01\x30\x01\x12>\n\x12getTaggedQuestions\x12\x13.QuestionPOSTagging\x1a\x13.QuestionPOSTaggingb\x06proto3'
)




_QUESTIONDETAILS = _descriptor.Descriptor(
  name='QuestionDetails',
  full_name='QuestionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='question', full_name='QuestionDetails.question', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='questionClass', full_name='QuestionDetails.questionClass', index=1,
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
  serialized_start=24,
  serialized_end=82,
)


_QUESTIONPOSTAGGING = _descriptor.Descriptor(
  name='QuestionPOSTagging',
  full_name='QuestionPOSTagging',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='questionDetails', full_name='QuestionPOSTagging.questionDetails', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taggedQuestion', full_name='QuestionPOSTagging.taggedQuestion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tagSequence', full_name='QuestionPOSTagging.tagSequence', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=84,
  serialized_end=192,
)


_GETQUESTIONSMESSAGE = _descriptor.Descriptor(
  name='GetQuestionsMessage',
  full_name='GetQuestionsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='GetQuestionsMessage.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='questionDetailsList', full_name='GetQuestionsMessage.questionDetailsList', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requestId', full_name='GetQuestionsMessage.requestId', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fromHost', full_name='GetQuestionsMessage.fromHost', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=194,
  serialized_end=314,
)

_QUESTIONPOSTAGGING.fields_by_name['questionDetails'].message_type = _QUESTIONDETAILS
_GETQUESTIONSMESSAGE.fields_by_name['questionDetailsList'].message_type = _QUESTIONDETAILS
DESCRIPTOR.message_types_by_name['QuestionDetails'] = _QUESTIONDETAILS
DESCRIPTOR.message_types_by_name['QuestionPOSTagging'] = _QUESTIONPOSTAGGING
DESCRIPTOR.message_types_by_name['GetQuestionsMessage'] = _GETQUESTIONSMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestionDetails = _reflection.GeneratedProtocolMessageType('QuestionDetails', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONDETAILS,
  '__module__' : 'sample_service_pb2'
  # @@protoc_insertion_point(class_scope:QuestionDetails)
  })
_sym_db.RegisterMessage(QuestionDetails)

QuestionPOSTagging = _reflection.GeneratedProtocolMessageType('QuestionPOSTagging', (_message.Message,), {
  'DESCRIPTOR' : _QUESTIONPOSTAGGING,
  '__module__' : 'sample_service_pb2'
  # @@protoc_insertion_point(class_scope:QuestionPOSTagging)
  })
_sym_db.RegisterMessage(QuestionPOSTagging)

GetQuestionsMessage = _reflection.GeneratedProtocolMessageType('GetQuestionsMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETQUESTIONSMESSAGE,
  '__module__' : 'sample_service_pb2'
  # @@protoc_insertion_point(class_scope:GetQuestionsMessage)
  })
_sym_db.RegisterMessage(GetQuestionsMessage)



_QUESTIONCLASSIFICATIONSERVICES = _descriptor.ServiceDescriptor(
  name='QuestionClassificationServices',
  full_name='QuestionClassificationServices',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=317,
  serialized_end=552,
  methods=[
  _descriptor.MethodDescriptor(
    name='getSampleQuestions',
    full_name='QuestionClassificationServices.getSampleQuestions',
    index=0,
    containing_service=None,
    input_type=_GETQUESTIONSMESSAGE,
    output_type=_GETQUESTIONSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='streamSampleQuestions',
    full_name='QuestionClassificationServices.streamSampleQuestions',
    index=1,
    containing_service=None,
    input_type=_GETQUESTIONSMESSAGE,
    output_type=_GETQUESTIONSMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getTaggedQuestions',
    full_name='QuestionClassificationServices.getTaggedQuestions',
    index=2,
    containing_service=None,
    input_type=_QUESTIONPOSTAGGING,
    output_type=_QUESTIONPOSTAGGING,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUESTIONCLASSIFICATIONSERVICES)

DESCRIPTOR.services_by_name['QuestionClassificationServices'] = _QUESTIONCLASSIFICATIONSERVICES

# @@protoc_insertion_point(module_scope)
