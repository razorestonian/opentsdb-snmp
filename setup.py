#!/usr/bin/env python
# This file is part of opentsdb-snmp.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.  This program is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser
# General Public License for more details.  You should have received a copy
# of the GNU Lesser General Public License along with this program.  If not,
# see <http://www.gnu.org/licenses/>.
import sys

sys.path.insert(0, "misc")

from distribute_setup import use_setuptools
use_setuptools()
import setuptools

import version

setuptools.setup(
    name="opentsdb.snmp",
    version=version.get_git_version(),
    namespace_packages=["opentsdb"],
    packages=setuptools.find_packages("src"),
    package_dir={
        "": "src",
    },
    package_data={
    },
    install_requires=[
        "netsnmp-python",
        "pyyaml"
    ],
    tests_require=[
        "nose>=1.0",
        "mock>=0.8."
    ],
    entry_points={
        "console_scripts": [
            "opentsdb-snmp=opentsdb.snmp.main:run"
        ],
        "resolvers": [
            "default=opentsdb.snmp.resolvers.default:Default",
            "ifname=opentsdb.snmp.resolvers.ifname:IfName",
            "direction_after_idx=opentsdb.snmp.resolvers.after_idx:AfterIndex",
            "d500_xdsl=opentsdb.snmp.resolvers.d500_xdsl:D500_xdsl",
        ],
        "value_modifiers": [
            "rate=opentsdb.snmp.value_modifiers.rate:Rate",
        ]
    },
    test_suite="nose.collector",

)
