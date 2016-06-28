#!/usr/bin/env python3
#
# Copyright (c) 2016 Roberto Riggio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

"""Virtual Base Station Point."""

from empower.core.pnfdev import BasePNFDev


class VBSP(BasePNFDev):
    """A Virtual Base Station Point.

    Attributes:
        addr: This PNFDev MAC address (EtherAddress)
        label: A human-radable description of this PNFDev (str)
        connection: Signalling channel connection (BasePNFPMainHandler)
        last_seen: Sequence number of the last hello message received (int)
        last_seen_ts: Timestamp of the last hello message received (int)
        feed: The power consumption monitoring feed (Feed)
        seq: Next sequence number (int)
        every: update period (in ms)
        uplink_bytes: signalling channel uplink bytes
        uplink_bit_rate: signalling channel uplink bit rate
        downlink_bytes: signalling channel downlink bytes
        downlink_bit_rate: signalling channel downlink bit rate
        ports: OVS ports
    """

    ALIAS = "vbsps"
    SOLO = "vbsp"

    def __init__(self, addr, label):
        super().__init__(addr, label)
        self.enb_config = None
        self.ues = {}

    def to_dict(self):
        """Return a JSON-serializable dictionary representing the VBSP."""

        out = super().to_dict()
        out['enb_config'] = self.enb_config,
        out['ues'] = self.ues

        return out