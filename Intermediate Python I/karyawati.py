
# -*- coding: utf-8 -*-
"""Karyawati.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gkpx6SO20-6GfpzJiMxXXsbx726PqpZE
"""

class Karyawati:
  nama_kantor = "DigitalSkola"
  def __init__(self, nama, umur, nomor_hp):
    self.nama = nama
    self._umur = umur
    self.__nomor_hp = nomor_hp

  def nama(self):
    return self.nama
  @property
  def umur(self):
    return self._umur

  @umur.setter
  def umur(self, umur):
    self._umur = umur

  @property
  def nomor_hp(self):
    return self.__nomor_hp

  @nomor_hp.setter
  def nomor_hp(self, nomor_hp):
    self.__nomor_hp = nomor_hp

karyawati.py
Displaying karyawati.py.