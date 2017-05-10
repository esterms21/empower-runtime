# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ran_sharing.proto

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
  name='ran_sharing.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x11ran_sharing.proto\"/\n\x10scheduling_param\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\t\"C\n\x10tenant_scheduler\x12\x0c\n\x04name\x18\x01 \x02(\t\x12!\n\x06params\x18\x02 \x03(\x0b\x32\x11.scheduling_param\"&\n\x11rbs_alloc_over_sf\x12\x11\n\trbs_alloc\x18\x01 \x03(\t\"\x1d\n\nadd_tenant\x12\x0f\n\x07plmn_id\x18\x01 \x02(\t\" \n\rremove_tenant\x12\x0f\n\x07plmn_id\x18\x01 \x02(\t\"@\n\rue_sched_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12!\n\x06params\x18\x02 \x03(\x0b\x32\x11.scheduling_param\"l\n\x0fue_sched_select\x12\x0f\n\x07plmn_id\x18\x01 \x02(\t\x12#\n\x0b\x64l_ue_sched\x18\x02 \x01(\x0b\x32\x0e.ue_sched_info\x12#\n\x0bul_ue_sched\x18\x03 \x01(\x0b\x32\x0e.ue_sched_info\"5\n\x0crbs_per_cell\x12\x14\n\x0cphys_cell_id\x18\x01 \x02(\r\x12\x0f\n\x07num_rbs\x18\x02 \x02(\x04\"_\n\x0etenant_rbs_req\x12\x0f\n\x07plmn_id\x18\x01 \x02(\t\x12\x1d\n\x06rbs_dl\x18\x02 \x03(\x0b\x32\r.rbs_per_cell\x12\x1d\n\x06rbs_ul\x18\x03 \x03(\x0b\x32\r.rbs_per_cell\"G\n\x13modify_sched_window\x12\x17\n\x0fsched_window_dl\x18\x01 \x01(\x04\x12\x17\n\x0fsched_window_ul\x18\x02 \x01(\x04\"J\n\x12rbs_alloc_per_cell\x12\x14\n\x0cphys_cell_id\x18\x01 \x02(\r\x12\x1e\n\x02sf\x18\x02 \x03(\x0b\x32\x12.rbs_alloc_over_sf\"9\n\x14static_tenants_sched\x12!\n\x04\x63\x65ll\x18\x01 \x03(\x0b\x32\x13.rbs_alloc_per_cell\"9\n\x15\x64ynamic_tenants_sched\x12 \n\x05sched\x18\x01 \x02(\x0b\x32\x11.tenant_scheduler\"Z\n\x13mixed_tenants_sched\x12!\n\x04\x63\x65ll\x18\x01 \x03(\x0b\x32\x13.rbs_alloc_per_cell\x12 \n\x05sched\x18\x02 \x02(\x0b\x32\x11.tenant_scheduler\"\xcb\x02\n\x14tenants_sched_select\x12\x30\n\x0fstatic_sched_dl\x18\x01 \x01(\x0b\x32\x15.static_tenants_schedH\x00\x12/\n\rdynm_sched_dl\x18\x02 \x01(\x0b\x32\x16.dynamic_tenants_schedH\x00\x12.\n\x0emixed_sched_dl\x18\x03 \x01(\x0b\x32\x14.mixed_tenants_schedH\x00\x12\x30\n\x0fstatic_sched_ul\x18\x04 \x01(\x0b\x32\x15.static_tenants_schedH\x00\x12/\n\rdynm_sched_ul\x18\x05 \x01(\x0b\x32\x16.dynamic_tenants_schedH\x00\x12.\n\x0emixed_sched_ul\x18\x06 \x01(\x0b\x32\x14.mixed_tenants_schedH\x00\x42\r\n\x0bsched_types\"\x91\x02\n\x14ran_sharing_ctrl_req\x12\x1c\n\x05\x61\x64\x64_t\x18\x01 \x01(\x0b\x32\x0b.add_tenantH\x00\x12\x1f\n\x05rem_t\x18\x02 \x01(\x0b\x32\x0e.remove_tenantH\x00\x12(\n\x0cue_sched_sel\x18\x03 \x01(\x0b\x32\x10.ue_sched_selectH\x00\x12$\n\tt_rbs_req\x18\x04 \x01(\x0b\x32\x0f.tenant_rbs_reqH\x00\x12,\n\x0bt_sched_sel\x18\x05 \x01(\x0b\x32\x15.tenants_sched_selectH\x00\x12\x30\n\x10mod_sched_window\x18\x06 \x01(\x0b\x32\x14.modify_sched_windowH\x00\x42\n\n\x08\x63trl_req\">\n\x15ran_sharing_ctrl_repl\x12%\n\x06status\x18\x01 \x02(\x0e\x32\x15.ran_share_req_status\"v\n\x10ran_sharing_ctrl\x12$\n\x03req\x18\x01 \x01(\x0b\x32\x15.ran_sharing_ctrl_reqH\x00\x12&\n\x04repl\x18\x02 \x01(\x0b\x32\x16.ran_sharing_ctrl_replH\x00\x42\x14\n\x12ran_sharing_ctrl_m*h\n\x14ran_share_req_status\x12\x18\n\x14RANSHARE_REQ_SUCCESS\x10\x00\x12\x18\n\x14RANSHARE_REQ_FAILURE\x10\x01\x12\x1c\n\x18RANSHARE_REQ_UNSUPPORTED\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_RAN_SHARE_REQ_STATUS = _descriptor.EnumDescriptor(
  name='ran_share_req_status',
  full_name='ran_share_req_status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RANSHARE_REQ_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANSHARE_REQ_FAILURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RANSHARE_REQ_UNSUPPORTED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1725,
  serialized_end=1829,
)
_sym_db.RegisterEnumDescriptor(_RAN_SHARE_REQ_STATUS)

ran_share_req_status = enum_type_wrapper.EnumTypeWrapper(_RAN_SHARE_REQ_STATUS)
RANSHARE_REQ_SUCCESS = 0
RANSHARE_REQ_FAILURE = 1
RANSHARE_REQ_UNSUPPORTED = 2



_SCHEDULING_PARAM = _descriptor.Descriptor(
  name='scheduling_param',
  full_name='scheduling_param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='scheduling_param.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='scheduling_param.value', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=68,
)


_TENANT_SCHEDULER = _descriptor.Descriptor(
  name='tenant_scheduler',
  full_name='tenant_scheduler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tenant_scheduler.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='tenant_scheduler.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=137,
)


_RBS_ALLOC_OVER_SF = _descriptor.Descriptor(
  name='rbs_alloc_over_sf',
  full_name='rbs_alloc_over_sf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rbs_alloc', full_name='rbs_alloc_over_sf.rbs_alloc', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=177,
)


_ADD_TENANT = _descriptor.Descriptor(
  name='add_tenant',
  full_name='add_tenant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plmn_id', full_name='add_tenant.plmn_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=208,
)


_REMOVE_TENANT = _descriptor.Descriptor(
  name='remove_tenant',
  full_name='remove_tenant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plmn_id', full_name='remove_tenant.plmn_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=242,
)


_UE_SCHED_INFO = _descriptor.Descriptor(
  name='ue_sched_info',
  full_name='ue_sched_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ue_sched_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='ue_sched_info.params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=308,
)


_UE_SCHED_SELECT = _descriptor.Descriptor(
  name='ue_sched_select',
  full_name='ue_sched_select',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plmn_id', full_name='ue_sched_select.plmn_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dl_ue_sched', full_name='ue_sched_select.dl_ue_sched', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ul_ue_sched', full_name='ue_sched_select.ul_ue_sched', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=418,
)


_RBS_PER_CELL = _descriptor.Descriptor(
  name='rbs_per_cell',
  full_name='rbs_per_cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phys_cell_id', full_name='rbs_per_cell.phys_cell_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_rbs', full_name='rbs_per_cell.num_rbs', index=1,
      number=2, type=4, cpp_type=4, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=420,
  serialized_end=473,
)


_TENANT_RBS_REQ = _descriptor.Descriptor(
  name='tenant_rbs_req',
  full_name='tenant_rbs_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plmn_id', full_name='tenant_rbs_req.plmn_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rbs_dl', full_name='tenant_rbs_req.rbs_dl', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rbs_ul', full_name='tenant_rbs_req.rbs_ul', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=475,
  serialized_end=570,
)


_MODIFY_SCHED_WINDOW = _descriptor.Descriptor(
  name='modify_sched_window',
  full_name='modify_sched_window',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sched_window_dl', full_name='modify_sched_window.sched_window_dl', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sched_window_ul', full_name='modify_sched_window.sched_window_ul', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=643,
)


_RBS_ALLOC_PER_CELL = _descriptor.Descriptor(
  name='rbs_alloc_per_cell',
  full_name='rbs_alloc_per_cell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phys_cell_id', full_name='rbs_alloc_per_cell.phys_cell_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sf', full_name='rbs_alloc_per_cell.sf', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=645,
  serialized_end=719,
)


_STATIC_TENANTS_SCHED = _descriptor.Descriptor(
  name='static_tenants_sched',
  full_name='static_tenants_sched',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell', full_name='static_tenants_sched.cell', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=721,
  serialized_end=778,
)


_DYNAMIC_TENANTS_SCHED = _descriptor.Descriptor(
  name='dynamic_tenants_sched',
  full_name='dynamic_tenants_sched',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sched', full_name='dynamic_tenants_sched.sched', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=837,
)


_MIXED_TENANTS_SCHED = _descriptor.Descriptor(
  name='mixed_tenants_sched',
  full_name='mixed_tenants_sched',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell', full_name='mixed_tenants_sched.cell', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sched', full_name='mixed_tenants_sched.sched', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=929,
)


_TENANTS_SCHED_SELECT = _descriptor.Descriptor(
  name='tenants_sched_select',
  full_name='tenants_sched_select',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='static_sched_dl', full_name='tenants_sched_select.static_sched_dl', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dynm_sched_dl', full_name='tenants_sched_select.dynm_sched_dl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mixed_sched_dl', full_name='tenants_sched_select.mixed_sched_dl', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='static_sched_ul', full_name='tenants_sched_select.static_sched_ul', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dynm_sched_ul', full_name='tenants_sched_select.dynm_sched_ul', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mixed_sched_ul', full_name='tenants_sched_select.mixed_sched_ul', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sched_types', full_name='tenants_sched_select.sched_types',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=932,
  serialized_end=1263,
)


_RAN_SHARING_CTRL_REQ = _descriptor.Descriptor(
  name='ran_sharing_ctrl_req',
  full_name='ran_sharing_ctrl_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='add_t', full_name='ran_sharing_ctrl_req.add_t', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rem_t', full_name='ran_sharing_ctrl_req.rem_t', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ue_sched_sel', full_name='ran_sharing_ctrl_req.ue_sched_sel', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_rbs_req', full_name='ran_sharing_ctrl_req.t_rbs_req', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t_sched_sel', full_name='ran_sharing_ctrl_req.t_sched_sel', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mod_sched_window', full_name='ran_sharing_ctrl_req.mod_sched_window', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ctrl_req', full_name='ran_sharing_ctrl_req.ctrl_req',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1266,
  serialized_end=1539,
)


_RAN_SHARING_CTRL_REPL = _descriptor.Descriptor(
  name='ran_sharing_ctrl_repl',
  full_name='ran_sharing_ctrl_repl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ran_sharing_ctrl_repl.status', index=0,
      number=1, type=14, cpp_type=8, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1541,
  serialized_end=1603,
)


_RAN_SHARING_CTRL = _descriptor.Descriptor(
  name='ran_sharing_ctrl',
  full_name='ran_sharing_ctrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='req', full_name='ran_sharing_ctrl.req', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repl', full_name='ran_sharing_ctrl.repl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ran_sharing_ctrl_m', full_name='ran_sharing_ctrl.ran_sharing_ctrl_m',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1605,
  serialized_end=1723,
)

_TENANT_SCHEDULER.fields_by_name['params'].message_type = _SCHEDULING_PARAM
_UE_SCHED_INFO.fields_by_name['params'].message_type = _SCHEDULING_PARAM
_UE_SCHED_SELECT.fields_by_name['dl_ue_sched'].message_type = _UE_SCHED_INFO
_UE_SCHED_SELECT.fields_by_name['ul_ue_sched'].message_type = _UE_SCHED_INFO
_TENANT_RBS_REQ.fields_by_name['rbs_dl'].message_type = _RBS_PER_CELL
_TENANT_RBS_REQ.fields_by_name['rbs_ul'].message_type = _RBS_PER_CELL
_RBS_ALLOC_PER_CELL.fields_by_name['sf'].message_type = _RBS_ALLOC_OVER_SF
_STATIC_TENANTS_SCHED.fields_by_name['cell'].message_type = _RBS_ALLOC_PER_CELL
_DYNAMIC_TENANTS_SCHED.fields_by_name['sched'].message_type = _TENANT_SCHEDULER
_MIXED_TENANTS_SCHED.fields_by_name['cell'].message_type = _RBS_ALLOC_PER_CELL
_MIXED_TENANTS_SCHED.fields_by_name['sched'].message_type = _TENANT_SCHEDULER
_TENANTS_SCHED_SELECT.fields_by_name['static_sched_dl'].message_type = _STATIC_TENANTS_SCHED
_TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_dl'].message_type = _DYNAMIC_TENANTS_SCHED
_TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_dl'].message_type = _MIXED_TENANTS_SCHED
_TENANTS_SCHED_SELECT.fields_by_name['static_sched_ul'].message_type = _STATIC_TENANTS_SCHED
_TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_ul'].message_type = _DYNAMIC_TENANTS_SCHED
_TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_ul'].message_type = _MIXED_TENANTS_SCHED
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['static_sched_dl'])
_TENANTS_SCHED_SELECT.fields_by_name['static_sched_dl'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_dl'])
_TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_dl'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_dl'])
_TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_dl'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['static_sched_ul'])
_TENANTS_SCHED_SELECT.fields_by_name['static_sched_ul'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_ul'])
_TENANTS_SCHED_SELECT.fields_by_name['dynm_sched_ul'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_TENANTS_SCHED_SELECT.oneofs_by_name['sched_types'].fields.append(
  _TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_ul'])
_TENANTS_SCHED_SELECT.fields_by_name['mixed_sched_ul'].containing_oneof = _TENANTS_SCHED_SELECT.oneofs_by_name['sched_types']
_RAN_SHARING_CTRL_REQ.fields_by_name['add_t'].message_type = _ADD_TENANT
_RAN_SHARING_CTRL_REQ.fields_by_name['rem_t'].message_type = _REMOVE_TENANT
_RAN_SHARING_CTRL_REQ.fields_by_name['ue_sched_sel'].message_type = _UE_SCHED_SELECT
_RAN_SHARING_CTRL_REQ.fields_by_name['t_rbs_req'].message_type = _TENANT_RBS_REQ
_RAN_SHARING_CTRL_REQ.fields_by_name['t_sched_sel'].message_type = _TENANTS_SCHED_SELECT
_RAN_SHARING_CTRL_REQ.fields_by_name['mod_sched_window'].message_type = _MODIFY_SCHED_WINDOW
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['add_t'])
_RAN_SHARING_CTRL_REQ.fields_by_name['add_t'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['rem_t'])
_RAN_SHARING_CTRL_REQ.fields_by_name['rem_t'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['ue_sched_sel'])
_RAN_SHARING_CTRL_REQ.fields_by_name['ue_sched_sel'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['t_rbs_req'])
_RAN_SHARING_CTRL_REQ.fields_by_name['t_rbs_req'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['t_sched_sel'])
_RAN_SHARING_CTRL_REQ.fields_by_name['t_sched_sel'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req'].fields.append(
  _RAN_SHARING_CTRL_REQ.fields_by_name['mod_sched_window'])
_RAN_SHARING_CTRL_REQ.fields_by_name['mod_sched_window'].containing_oneof = _RAN_SHARING_CTRL_REQ.oneofs_by_name['ctrl_req']
_RAN_SHARING_CTRL_REPL.fields_by_name['status'].enum_type = _RAN_SHARE_REQ_STATUS
_RAN_SHARING_CTRL.fields_by_name['req'].message_type = _RAN_SHARING_CTRL_REQ
_RAN_SHARING_CTRL.fields_by_name['repl'].message_type = _RAN_SHARING_CTRL_REPL
_RAN_SHARING_CTRL.oneofs_by_name['ran_sharing_ctrl_m'].fields.append(
  _RAN_SHARING_CTRL.fields_by_name['req'])
_RAN_SHARING_CTRL.fields_by_name['req'].containing_oneof = _RAN_SHARING_CTRL.oneofs_by_name['ran_sharing_ctrl_m']
_RAN_SHARING_CTRL.oneofs_by_name['ran_sharing_ctrl_m'].fields.append(
  _RAN_SHARING_CTRL.fields_by_name['repl'])
_RAN_SHARING_CTRL.fields_by_name['repl'].containing_oneof = _RAN_SHARING_CTRL.oneofs_by_name['ran_sharing_ctrl_m']
DESCRIPTOR.message_types_by_name['scheduling_param'] = _SCHEDULING_PARAM
DESCRIPTOR.message_types_by_name['tenant_scheduler'] = _TENANT_SCHEDULER
DESCRIPTOR.message_types_by_name['rbs_alloc_over_sf'] = _RBS_ALLOC_OVER_SF
DESCRIPTOR.message_types_by_name['add_tenant'] = _ADD_TENANT
DESCRIPTOR.message_types_by_name['remove_tenant'] = _REMOVE_TENANT
DESCRIPTOR.message_types_by_name['ue_sched_info'] = _UE_SCHED_INFO
DESCRIPTOR.message_types_by_name['ue_sched_select'] = _UE_SCHED_SELECT
DESCRIPTOR.message_types_by_name['rbs_per_cell'] = _RBS_PER_CELL
DESCRIPTOR.message_types_by_name['tenant_rbs_req'] = _TENANT_RBS_REQ
DESCRIPTOR.message_types_by_name['modify_sched_window'] = _MODIFY_SCHED_WINDOW
DESCRIPTOR.message_types_by_name['rbs_alloc_per_cell'] = _RBS_ALLOC_PER_CELL
DESCRIPTOR.message_types_by_name['static_tenants_sched'] = _STATIC_TENANTS_SCHED
DESCRIPTOR.message_types_by_name['dynamic_tenants_sched'] = _DYNAMIC_TENANTS_SCHED
DESCRIPTOR.message_types_by_name['mixed_tenants_sched'] = _MIXED_TENANTS_SCHED
DESCRIPTOR.message_types_by_name['tenants_sched_select'] = _TENANTS_SCHED_SELECT
DESCRIPTOR.message_types_by_name['ran_sharing_ctrl_req'] = _RAN_SHARING_CTRL_REQ
DESCRIPTOR.message_types_by_name['ran_sharing_ctrl_repl'] = _RAN_SHARING_CTRL_REPL
DESCRIPTOR.message_types_by_name['ran_sharing_ctrl'] = _RAN_SHARING_CTRL
DESCRIPTOR.enum_types_by_name['ran_share_req_status'] = _RAN_SHARE_REQ_STATUS

scheduling_param = _reflection.GeneratedProtocolMessageType('scheduling_param', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULING_PARAM,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:scheduling_param)
  ))
_sym_db.RegisterMessage(scheduling_param)

tenant_scheduler = _reflection.GeneratedProtocolMessageType('tenant_scheduler', (_message.Message,), dict(
  DESCRIPTOR = _TENANT_SCHEDULER,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:tenant_scheduler)
  ))
_sym_db.RegisterMessage(tenant_scheduler)

rbs_alloc_over_sf = _reflection.GeneratedProtocolMessageType('rbs_alloc_over_sf', (_message.Message,), dict(
  DESCRIPTOR = _RBS_ALLOC_OVER_SF,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:rbs_alloc_over_sf)
  ))
_sym_db.RegisterMessage(rbs_alloc_over_sf)

add_tenant = _reflection.GeneratedProtocolMessageType('add_tenant', (_message.Message,), dict(
  DESCRIPTOR = _ADD_TENANT,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:add_tenant)
  ))
_sym_db.RegisterMessage(add_tenant)

remove_tenant = _reflection.GeneratedProtocolMessageType('remove_tenant', (_message.Message,), dict(
  DESCRIPTOR = _REMOVE_TENANT,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:remove_tenant)
  ))
_sym_db.RegisterMessage(remove_tenant)

ue_sched_info = _reflection.GeneratedProtocolMessageType('ue_sched_info', (_message.Message,), dict(
  DESCRIPTOR = _UE_SCHED_INFO,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:ue_sched_info)
  ))
_sym_db.RegisterMessage(ue_sched_info)

ue_sched_select = _reflection.GeneratedProtocolMessageType('ue_sched_select', (_message.Message,), dict(
  DESCRIPTOR = _UE_SCHED_SELECT,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:ue_sched_select)
  ))
_sym_db.RegisterMessage(ue_sched_select)

rbs_per_cell = _reflection.GeneratedProtocolMessageType('rbs_per_cell', (_message.Message,), dict(
  DESCRIPTOR = _RBS_PER_CELL,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:rbs_per_cell)
  ))
_sym_db.RegisterMessage(rbs_per_cell)

tenant_rbs_req = _reflection.GeneratedProtocolMessageType('tenant_rbs_req', (_message.Message,), dict(
  DESCRIPTOR = _TENANT_RBS_REQ,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:tenant_rbs_req)
  ))
_sym_db.RegisterMessage(tenant_rbs_req)

modify_sched_window = _reflection.GeneratedProtocolMessageType('modify_sched_window', (_message.Message,), dict(
  DESCRIPTOR = _MODIFY_SCHED_WINDOW,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:modify_sched_window)
  ))
_sym_db.RegisterMessage(modify_sched_window)

rbs_alloc_per_cell = _reflection.GeneratedProtocolMessageType('rbs_alloc_per_cell', (_message.Message,), dict(
  DESCRIPTOR = _RBS_ALLOC_PER_CELL,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:rbs_alloc_per_cell)
  ))
_sym_db.RegisterMessage(rbs_alloc_per_cell)

static_tenants_sched = _reflection.GeneratedProtocolMessageType('static_tenants_sched', (_message.Message,), dict(
  DESCRIPTOR = _STATIC_TENANTS_SCHED,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:static_tenants_sched)
  ))
_sym_db.RegisterMessage(static_tenants_sched)

dynamic_tenants_sched = _reflection.GeneratedProtocolMessageType('dynamic_tenants_sched', (_message.Message,), dict(
  DESCRIPTOR = _DYNAMIC_TENANTS_SCHED,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:dynamic_tenants_sched)
  ))
_sym_db.RegisterMessage(dynamic_tenants_sched)

mixed_tenants_sched = _reflection.GeneratedProtocolMessageType('mixed_tenants_sched', (_message.Message,), dict(
  DESCRIPTOR = _MIXED_TENANTS_SCHED,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:mixed_tenants_sched)
  ))
_sym_db.RegisterMessage(mixed_tenants_sched)

tenants_sched_select = _reflection.GeneratedProtocolMessageType('tenants_sched_select', (_message.Message,), dict(
  DESCRIPTOR = _TENANTS_SCHED_SELECT,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:tenants_sched_select)
  ))
_sym_db.RegisterMessage(tenants_sched_select)

ran_sharing_ctrl_req = _reflection.GeneratedProtocolMessageType('ran_sharing_ctrl_req', (_message.Message,), dict(
  DESCRIPTOR = _RAN_SHARING_CTRL_REQ,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:ran_sharing_ctrl_req)
  ))
_sym_db.RegisterMessage(ran_sharing_ctrl_req)

ran_sharing_ctrl_repl = _reflection.GeneratedProtocolMessageType('ran_sharing_ctrl_repl', (_message.Message,), dict(
  DESCRIPTOR = _RAN_SHARING_CTRL_REPL,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:ran_sharing_ctrl_repl)
  ))
_sym_db.RegisterMessage(ran_sharing_ctrl_repl)

ran_sharing_ctrl = _reflection.GeneratedProtocolMessageType('ran_sharing_ctrl', (_message.Message,), dict(
  DESCRIPTOR = _RAN_SHARING_CTRL,
  __module__ = 'ran_sharing_pb2'
  # @@protoc_insertion_point(class_scope:ran_sharing_ctrl)
  ))
_sym_db.RegisterMessage(ran_sharing_ctrl)


# @@protoc_insertion_point(module_scope)