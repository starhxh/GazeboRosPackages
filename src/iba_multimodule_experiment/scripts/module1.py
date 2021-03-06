#!/usr/bin/env python
""" """

__author__ = 'Omer Yilmaz'

import rospy
from external_module_interface.external_module import ExternalModule


class Module1(ExternalModule):
    
    def __init__(self, module_name=None, steps=1):
        super(Module1, self).__init__(module_name, steps)
    
    # def initialize(self):
    #     pass
    
    def run_step(self): 
        pass

    # def shutdown(self):
    #     pass

    def share_module_data(self):
        self.module_data = [1, 2.50, -3.7]

if __name__ == "__main__":
    m = Module1(module_name='module1', steps=4)
    rospy.spin()
