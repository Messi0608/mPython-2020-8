# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:25:25 2020

@author: AE401
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
print(mc.player.getTilePos())