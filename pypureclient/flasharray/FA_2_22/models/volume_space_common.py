# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_22 import models

class VolumeSpaceCommon(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'data_reduction': 'float',
        'shared': 'int',
        'snapshots': 'int',
        'system': 'int',
        'thin_provisioning': 'float',
        'total_physical': 'int',
        'total_provisioned': 'int',
        'total_reduction': 'float',
        'unique': 'int',
        'virtual': 'int',
        'snapshots_effective': 'int',
        'unique_effective': 'int',
        'total_effective': 'int'
    }

    attribute_map = {
        'data_reduction': 'data_reduction',
        'shared': 'shared',
        'snapshots': 'snapshots',
        'system': 'system',
        'thin_provisioning': 'thin_provisioning',
        'total_physical': 'total_physical',
        'total_provisioned': 'total_provisioned',
        'total_reduction': 'total_reduction',
        'unique': 'unique',
        'virtual': 'virtual',
        'snapshots_effective': 'snapshots_effective',
        'unique_effective': 'unique_effective',
        'total_effective': 'total_effective'
    }

    required_args = {
    }

    def __init__(
        self,
        data_reduction=None,  # type: float
        shared=None,  # type: int
        snapshots=None,  # type: int
        system=None,  # type: int
        thin_provisioning=None,  # type: float
        total_physical=None,  # type: int
        total_provisioned=None,  # type: int
        total_reduction=None,  # type: float
        unique=None,  # type: int
        virtual=None,  # type: int
        snapshots_effective=None,  # type: int
        unique_effective=None,  # type: int
        total_effective=None,  # type: int
    ):
        """
        Keyword args:
            data_reduction (float): The ratio of mapped sectors within a volume versus the amount of physical space the data occupies after data compression and deduplication. The data reduction ratio does not include thin provisioning savings. For example, a data reduction ratio of 5&#58;1 means that for every 5 MB the host writes to the array, 1 MB is stored on the array's flash modules.
            shared (int): The physical space occupied by deduplicated data, meaning that the space is shared with other volumes and snapshots as a result of data deduplication. Measured in bytes.
            snapshots (int): The physical space occupied by data unique to one or more snapshots. Measured in bytes.
            system (int): The physical space occupied by internal array metadata. Measured in bytes.
            thin_provisioning (float): The percentage of volume sectors that do not contain host-written data because the hosts have not written data to them or the sectors have been explicitly trimmed.
            total_physical (int): The total physical space occupied by system, shared space, volume, and snapshot data. Measured in bytes.
            total_provisioned (int): For a single volume, the provisioned size of the volume. For all other resources, the total provisioned size of all volumes that are connected to or are inside the resource. Represents storage capacity reported to hosts. Measured in bytes.
            total_reduction (float): The ratio of provisioned sectors within a volume versus the amount of physical space the data occupies after reduction via data compression and deduplication and with thin provisioning savings. Total reduction is data reduction with thin provisioning savings. For example, a total reduction ratio of 10&#58;1 means that for every 10 MB of provisioned space, 1 MB is stored on the array's flash modules.
            unique (int): The unique physical space occupied by customer data. Unique physical space does not include shared space, snapshots, and internal array metadata. Measured in bytes.
            virtual (int): The amount of logically written data that a volume or a snapshot references. Measured in bytes.
            snapshots_effective (int): The effective space contributed by data unique to one or more snapshots, measured in bytes.
            unique_effective (int): The effective space contributed by unique customer data. Unique data does not include shared space, snapshots, and internal array metadata, measured in bytes.
            total_effective (int): The total effective space contributed by customer data, measured in bytes.
        """
        if data_reduction is not None:
            self.data_reduction = data_reduction
        if shared is not None:
            self.shared = shared
        if snapshots is not None:
            self.snapshots = snapshots
        if system is not None:
            self.system = system
        if thin_provisioning is not None:
            self.thin_provisioning = thin_provisioning
        if total_physical is not None:
            self.total_physical = total_physical
        if total_provisioned is not None:
            self.total_provisioned = total_provisioned
        if total_reduction is not None:
            self.total_reduction = total_reduction
        if unique is not None:
            self.unique = unique
        if virtual is not None:
            self.virtual = virtual
        if snapshots_effective is not None:
            self.snapshots_effective = snapshots_effective
        if unique_effective is not None:
            self.unique_effective = unique_effective
        if total_effective is not None:
            self.total_effective = total_effective

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `VolumeSpaceCommon`".format(key))
        if key == "shared" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `shared`, must be a value greater than or equal to `0`")
        if key == "snapshots" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `snapshots`, must be a value greater than or equal to `0`")
        if key == "system" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `system`, must be a value greater than or equal to `0`")
        if key == "thin_provisioning" and value is not None:
            if value > 1.0:
                raise ValueError("Invalid value for `thin_provisioning`, value must be less than or equal to `1.0`")
            if value < 0.0:
                raise ValueError("Invalid value for `thin_provisioning`, must be a value greater than or equal to `0.0`")
        if key == "total_physical" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_physical`, must be a value greater than or equal to `0`")
        if key == "total_provisioned" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_provisioned`, must be a value greater than or equal to `0`")
        if key == "unique" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `unique`, must be a value greater than or equal to `0`")
        if key == "virtual" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `virtual`, must be a value greater than or equal to `0`")
        if key == "snapshots_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `snapshots_effective`, must be a value greater than or equal to `0`")
        if key == "unique_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `unique_effective`, must be a value greater than or equal to `0`")
        if key == "total_effective" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_effective`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(VolumeSpaceCommon, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VolumeSpaceCommon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
