# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "oracle-database autonomous-database switchover",
)
class Switchover(AAZCommand):
    """Perform switchover action on Autonomous Database

    :example: Switchover
        az oracle-database autonomous-database switchover --autonomousdatabasename <ADBS name> --resource-group <resource_group> --peer-db-id <id>
    """

    _aaz_info = {
        "version": "2023-09-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/oracle.database/autonomousdatabases/{}/switchover", "2023-09-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.autonomousdatabasename = AAZStrArg(
            options=["--autonomousdatabasename"],
            help="The database name.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern=".*",
                max_length=30,
                min_length=1,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.peer_db_id = AAZStrArg(
            options=["--peer-db-id"],
            arg_group="Body",
            help="The database OCID of the Disaster Recovery peer database, which is located in a different region from the current peer database.",
            fmt=AAZStrArgFormat(
                max_length=255,
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.AutonomousDatabasesSwitchover(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class AutonomousDatabasesSwitchover(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Oracle.Database/autonomousDatabases/{autonomousdatabasename}/switchover",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "autonomousdatabasename", self.ctx.args.autonomousdatabasename,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-09-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("peerDbId", AAZStrType, ".peer_db_id")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.actual_used_data_storage_size_in_tbs = AAZFloatType(
                serialized_name="actualUsedDataStorageSizeInTbs",
                flags={"read_only": True},
            )
            properties.allocated_storage_size_in_tbs = AAZFloatType(
                serialized_name="allocatedStorageSizeInTbs",
                flags={"read_only": True},
            )
            properties.apex_details = AAZObjectType(
                serialized_name="apexDetails",
            )
            properties.autonomous_database_id = AAZStrType(
                serialized_name="autonomousDatabaseId",
            )
            properties.autonomous_maintenance_schedule_type = AAZStrType(
                serialized_name="autonomousMaintenanceScheduleType",
            )
            properties.available_upgrade_versions = AAZListType(
                serialized_name="availableUpgradeVersions",
                flags={"read_only": True},
            )
            properties.backup_retention_period_in_days = AAZIntType(
                serialized_name="backupRetentionPeriodInDays",
            )
            properties.character_set = AAZStrType(
                serialized_name="characterSet",
            )
            properties.compute_count = AAZFloatType(
                serialized_name="computeCount",
            )
            properties.compute_model = AAZStrType(
                serialized_name="computeModel",
            )
            properties.connection_strings = AAZObjectType(
                serialized_name="connectionStrings",
            )
            properties.connection_urls = AAZObjectType(
                serialized_name="connectionUrls",
            )
            properties.cpu_core_count = AAZIntType(
                serialized_name="cpuCoreCount",
            )
            properties.customer_contacts = AAZListType(
                serialized_name="customerContacts",
            )
            properties.data_base_type = AAZStrType(
                serialized_name="dataBaseType",
            )
            properties.data_safe_status = AAZStrType(
                serialized_name="dataSafeStatus",
            )
            properties.data_storage_size_in_gbs = AAZIntType(
                serialized_name="dataStorageSizeInGbs",
            )
            properties.data_storage_size_in_tbs = AAZIntType(
                serialized_name="dataStorageSizeInTbs",
            )
            properties.database_edition = AAZStrType(
                serialized_name="databaseEdition",
            )
            properties.db_version = AAZStrType(
                serialized_name="dbVersion",
            )
            properties.db_workload = AAZStrType(
                serialized_name="dbWorkload",
            )
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.failed_data_recovery_in_seconds = AAZIntType(
                serialized_name="failedDataRecoveryInSeconds",
                flags={"read_only": True},
            )
            properties.in_memory_area_in_gbs = AAZIntType(
                serialized_name="inMemoryAreaInGbs",
                flags={"read_only": True},
            )
            properties.is_auto_scaling_enabled = AAZBoolType(
                serialized_name="isAutoScalingEnabled",
            )
            properties.is_auto_scaling_for_storage_enabled = AAZBoolType(
                serialized_name="isAutoScalingForStorageEnabled",
            )
            properties.is_local_data_guard_enabled = AAZBoolType(
                serialized_name="isLocalDataGuardEnabled",
            )
            properties.is_mtls_connection_required = AAZBoolType(
                serialized_name="isMtlsConnectionRequired",
            )
            properties.is_preview = AAZBoolType(
                serialized_name="isPreview",
                flags={"read_only": True},
            )
            properties.is_remote_data_guard_enabled = AAZBoolType(
                serialized_name="isRemoteDataGuardEnabled",
                flags={"read_only": True},
            )
            properties.license_model = AAZStrType(
                serialized_name="licenseModel",
            )
            properties.lifecycle_details = AAZStrType(
                serialized_name="lifecycleDetails",
                flags={"read_only": True},
            )
            properties.lifecycle_state = AAZStrType(
                serialized_name="lifecycleState",
            )
            properties.local_adg_auto_failover_max_data_loss_limit = AAZIntType(
                serialized_name="localAdgAutoFailoverMaxDataLossLimit",
            )
            properties.local_disaster_recovery_type = AAZStrType(
                serialized_name="localDisasterRecoveryType",
            )
            properties.local_standby_db = AAZObjectType(
                serialized_name="localStandbyDb",
            )
            properties.long_term_backup_schedule = AAZObjectType(
                serialized_name="longTermBackupSchedule",
            )
            properties.memory_per_oracle_compute_unit_in_gbs = AAZIntType(
                serialized_name="memoryPerOracleComputeUnitInGbs",
                flags={"read_only": True},
            )
            properties.ncharacter_set = AAZStrType(
                serialized_name="ncharacterSet",
            )
            properties.next_long_term_backup_time_stamp = AAZStrType(
                serialized_name="nextLongTermBackupTimeStamp",
                flags={"read_only": True},
            )
            properties.oci_url = AAZStrType(
                serialized_name="ociUrl",
                flags={"read_only": True},
            )
            properties.ocid = AAZStrType()
            properties.open_mode = AAZStrType(
                serialized_name="openMode",
            )
            properties.operations_insights_status = AAZStrType(
                serialized_name="operationsInsightsStatus",
            )
            properties.peer_db_ids = AAZListType(
                serialized_name="peerDbIds",
                flags={"read_only": True},
            )
            properties.permission_level = AAZStrType(
                serialized_name="permissionLevel",
            )
            properties.private_endpoint = AAZStrType(
                serialized_name="privateEndpoint",
                flags={"read_only": True},
            )
            properties.private_endpoint_ip = AAZStrType(
                serialized_name="privateEndpointIp",
            )
            properties.private_endpoint_label = AAZStrType(
                serialized_name="privateEndpointLabel",
            )
            properties.provisionable_cpus = AAZListType(
                serialized_name="provisionableCpus",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.role = AAZStrType()
            properties.scheduled_operations = AAZObjectType(
                serialized_name="scheduledOperations",
            )
            properties.service_console_url = AAZStrType(
                serialized_name="serviceConsoleUrl",
                flags={"read_only": True},
            )
            properties.sql_web_developer_url = AAZStrType(
                serialized_name="sqlWebDeveloperUrl",
                flags={"read_only": True},
            )
            properties.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )
            properties.supported_regions_to_clone_to = AAZListType(
                serialized_name="supportedRegionsToCloneTo",
                flags={"read_only": True},
            )
            properties.time_created = AAZStrType(
                serialized_name="timeCreated",
                flags={"read_only": True},
            )
            properties.time_data_guard_role_changed = AAZStrType(
                serialized_name="timeDataGuardRoleChanged",
                flags={"read_only": True},
            )
            properties.time_deletion_of_free_autonomous_database = AAZStrType(
                serialized_name="timeDeletionOfFreeAutonomousDatabase",
                flags={"read_only": True},
            )
            properties.time_local_data_guard_enabled = AAZStrType(
                serialized_name="timeLocalDataGuardEnabled",
                flags={"read_only": True},
            )
            properties.time_maintenance_begin = AAZStrType(
                serialized_name="timeMaintenanceBegin",
                flags={"read_only": True},
            )
            properties.time_maintenance_end = AAZStrType(
                serialized_name="timeMaintenanceEnd",
                flags={"read_only": True},
            )
            properties.time_of_last_failover = AAZStrType(
                serialized_name="timeOfLastFailover",
                flags={"read_only": True},
            )
            properties.time_of_last_refresh = AAZStrType(
                serialized_name="timeOfLastRefresh",
                flags={"read_only": True},
            )
            properties.time_of_last_refresh_point = AAZStrType(
                serialized_name="timeOfLastRefreshPoint",
                flags={"read_only": True},
            )
            properties.time_of_last_switchover = AAZStrType(
                serialized_name="timeOfLastSwitchover",
                flags={"read_only": True},
            )
            properties.time_reclamation_of_free_autonomous_database = AAZStrType(
                serialized_name="timeReclamationOfFreeAutonomousDatabase",
                flags={"read_only": True},
            )
            properties.used_data_storage_size_in_gbs = AAZIntType(
                serialized_name="usedDataStorageSizeInGbs",
                flags={"read_only": True},
            )
            properties.used_data_storage_size_in_tbs = AAZIntType(
                serialized_name="usedDataStorageSizeInTbs",
                flags={"read_only": True},
            )
            properties.vnet_id = AAZStrType(
                serialized_name="vnetId",
            )
            properties.whitelisted_ips = AAZListType(
                serialized_name="whitelistedIps",
            )

            apex_details = cls._schema_on_200.properties.apex_details
            apex_details.apex_version = AAZStrType(
                serialized_name="apexVersion",
            )
            apex_details.ords_version = AAZStrType(
                serialized_name="ordsVersion",
            )

            available_upgrade_versions = cls._schema_on_200.properties.available_upgrade_versions
            available_upgrade_versions.Element = AAZStrType()

            connection_strings = cls._schema_on_200.properties.connection_strings
            connection_strings.all_connection_strings = AAZObjectType(
                serialized_name="allConnectionStrings",
            )
            connection_strings.dedicated = AAZStrType()
            connection_strings.high = AAZStrType()
            connection_strings.low = AAZStrType()
            connection_strings.medium = AAZStrType()
            connection_strings.profiles = AAZListType()

            all_connection_strings = cls._schema_on_200.properties.connection_strings.all_connection_strings
            all_connection_strings.high = AAZStrType()
            all_connection_strings.low = AAZStrType()
            all_connection_strings.medium = AAZStrType()

            profiles = cls._schema_on_200.properties.connection_strings.profiles
            profiles.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.connection_strings.profiles.Element
            _element.consumer_group = AAZStrType(
                serialized_name="consumerGroup",
            )
            _element.display_name = AAZStrType(
                serialized_name="displayName",
                flags={"required": True},
            )
            _element.host_format = AAZStrType(
                serialized_name="hostFormat",
                flags={"required": True},
            )
            _element.is_regional = AAZBoolType(
                serialized_name="isRegional",
            )
            _element.protocol = AAZStrType(
                flags={"required": True},
            )
            _element.session_mode = AAZStrType(
                serialized_name="sessionMode",
                flags={"required": True},
            )
            _element.syntax_format = AAZStrType(
                serialized_name="syntaxFormat",
                flags={"required": True},
            )
            _element.tls_authentication = AAZStrType(
                serialized_name="tlsAuthentication",
            )
            _element.value = AAZStrType(
                flags={"required": True},
            )

            connection_urls = cls._schema_on_200.properties.connection_urls
            connection_urls.apex_url = AAZStrType(
                serialized_name="apexUrl",
            )
            connection_urls.database_transforms_url = AAZStrType(
                serialized_name="databaseTransformsUrl",
            )
            connection_urls.graph_studio_url = AAZStrType(
                serialized_name="graphStudioUrl",
            )
            connection_urls.machine_learning_notebook_url = AAZStrType(
                serialized_name="machineLearningNotebookUrl",
            )
            connection_urls.mongo_db_url = AAZStrType(
                serialized_name="mongoDbUrl",
            )
            connection_urls.ords_url = AAZStrType(
                serialized_name="ordsUrl",
            )
            connection_urls.sql_dev_web_url = AAZStrType(
                serialized_name="sqlDevWebUrl",
            )

            customer_contacts = cls._schema_on_200.properties.customer_contacts
            customer_contacts.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.customer_contacts.Element
            _element.email = AAZStrType(
                flags={"required": True},
            )

            local_standby_db = cls._schema_on_200.properties.local_standby_db
            local_standby_db.lag_time_in_seconds = AAZIntType(
                serialized_name="lagTimeInSeconds",
            )
            local_standby_db.lifecycle_details = AAZStrType(
                serialized_name="lifecycleDetails",
            )
            local_standby_db.lifecycle_state = AAZStrType(
                serialized_name="lifecycleState",
            )
            local_standby_db.time_data_guard_role_changed = AAZStrType(
                serialized_name="timeDataGuardRoleChanged",
            )
            local_standby_db.time_disaster_recovery_role_changed = AAZStrType(
                serialized_name="timeDisasterRecoveryRoleChanged",
            )

            long_term_backup_schedule = cls._schema_on_200.properties.long_term_backup_schedule
            long_term_backup_schedule.is_disabled = AAZBoolType(
                serialized_name="isDisabled",
            )
            long_term_backup_schedule.repeat_cadence = AAZStrType(
                serialized_name="repeatCadence",
            )
            long_term_backup_schedule.retention_period_in_days = AAZIntType(
                serialized_name="retentionPeriodInDays",
            )
            long_term_backup_schedule.time_of_backup = AAZStrType(
                serialized_name="timeOfBackup",
            )

            peer_db_ids = cls._schema_on_200.properties.peer_db_ids
            peer_db_ids.Element = AAZStrType()

            provisionable_cpus = cls._schema_on_200.properties.provisionable_cpus
            provisionable_cpus.Element = AAZIntType()

            scheduled_operations = cls._schema_on_200.properties.scheduled_operations
            scheduled_operations.day_of_week = AAZObjectType(
                serialized_name="dayOfWeek",
                flags={"required": True},
            )
            scheduled_operations.scheduled_start_time = AAZStrType(
                serialized_name="scheduledStartTime",
            )
            scheduled_operations.scheduled_stop_time = AAZStrType(
                serialized_name="scheduledStopTime",
            )

            day_of_week = cls._schema_on_200.properties.scheduled_operations.day_of_week
            day_of_week.name = AAZStrType(
                flags={"required": True},
            )

            supported_regions_to_clone_to = cls._schema_on_200.properties.supported_regions_to_clone_to
            supported_regions_to_clone_to.Element = AAZStrType()

            whitelisted_ips = cls._schema_on_200.properties.whitelisted_ips
            whitelisted_ips.Element = AAZStrType()

            disc_clone = cls._schema_on_200.properties.discriminate_by("data_base_type", "Clone")
            disc_clone.is_reconnect_clone_enabled = AAZBoolType(
                serialized_name="isReconnectCloneEnabled",
                flags={"read_only": True},
            )
            disc_clone.is_refreshable_clone = AAZBoolType(
                serialized_name="isRefreshableClone",
                flags={"read_only": True},
            )
            disc_clone.refreshable_status = AAZStrType(
                serialized_name="refreshableStatus",
            )
            disc_clone.source_id = AAZStrType(
                serialized_name="sourceId",
                flags={"required": True},
            )
            disc_clone.time_until_reconnect_clone_enabled = AAZStrType(
                serialized_name="timeUntilReconnectCloneEnabled",
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _SwitchoverHelper:
    """Helper class for Switchover"""


__all__ = ["Switchover"]
