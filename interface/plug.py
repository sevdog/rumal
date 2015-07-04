#!/usr/bin/env python
#
# views.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA
#
# Author:   Tarun Kumar <reach.tarun.here@gmail.com
#

import abc

class UnmetDependencyError(Exception): 
    value = "Dependency %s was not met."

class PluginBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractproperty
    def dependencies(self):
        """List of dependencies - put class names of required plugins here.
           Return blank list if none."""
        return []

    def input_run(self,data):
        """Adds data to object and calls self.run"""
        self.data = data

    def save_data(self):
        """Add to plugins list and return modified data."""
        if self.__class__.__name__ not self.data["Plugins"]:
            self.data["Plugins"].append(self.__class__.__name__)
        return self.data

    def check_dependencies(self):
        """Check if all the dependencies are met."""
        for x in self.dependencies:
            if x not self.data["Plugins"]:
                raise UnmetDependenyError, UnmetDependenyError.value % x

    @abc.abstractmethod
    def run(self):
        """Run and make changes to data"""
        #1. Call check for dependencies
        self.check_dependencies()
        #2. Append all changes to x.data["flat_tree"]["url_link/node"]["plugin_name"]
        #3. Call save data
        self.save_data()

    def search(self):
        pass
