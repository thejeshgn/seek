# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='nsjail_programming_server',
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x19nsjail_programming_server\"Q\n\x0eResourceLimits\x12\x12\n\ntime_limit\x18\x03 \x01(\x05\x12\x15\n\rprocess_limit\x18\x04 \x01(\x05\x12\x14\n\x0cmemory_limit\x18\x05 \x01(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESOURCELIMITS = _descriptor.Descriptor(
  name='ResourceLimits',
  full_name='nsjail_programming_server.ResourceLimits',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_limit', full_name='nsjail_programming_server.ResourceLimits.time_limit', index=0,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='process_limit', full_name='nsjail_programming_server.ResourceLimits.process_limit', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_limit', full_name='nsjail_programming_server.ResourceLimits.memory_limit', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=124,
)

DESCRIPTOR.message_types_by_name['ResourceLimits'] = _RESOURCELIMITS

ResourceLimits = _reflection.GeneratedProtocolMessageType('ResourceLimits', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCELIMITS,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:nsjail_programming_server.ResourceLimits)
  ))
_sym_db.RegisterMessage(ResourceLimits)


# @@protoc_insertion_point(module_scope)
