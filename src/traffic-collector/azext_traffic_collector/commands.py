# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

# from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):  # pylint: disable=unused-argument
    with self.command_group("network-function traffic-collector collector-policy"):
        from .custom import CollectorPolicyCreate
        from .custom import CollectorPolicyUpdate
        self.command_table["network-function traffic-collector collector-policy create"] = \
            CollectorPolicyCreate(loader=self)
        self.command_table["network-function traffic-collector collector-policy update"] = \
            CollectorPolicyUpdate(loader=self)
