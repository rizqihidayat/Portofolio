Main Menu
Data Engineer 5
Homework - Intermediate Python I Python OOP, Class and Object
Digital Skola03
•
Feb 5
100/100
100 points out of possible 100
Due Feb 9, 11:59 PM
Homework ini merupakan tugas INDIVIDU
Buat class ‘Karyawan’ yang memiliki class attributes 'nama_kantor' dan instance attributes 'nama'
(public),  'umur' (protected) dan ‘nomor_hp’ (private).
Dalam class ‘Karyawan’ memiliki method ‘nomor_hp’, buat fungsi yang menggunakan accessor dan mutator untuk mengakses dan mengatur attributes ‘nomor_hp’.
Simpan class tersebut dengan nama karyawan.py
Buat class ‘Karyawati’ yang memiliki class attributes 'nama_kantor' dan instance attributes 'nama'
(public),  'umur' (protected) dan ‘nomor_hp’ (private)
Dalam class ‘Karyawati’ memiliki method ‘nomor_hp’, buat fungsi yang menggunakan accessor dan mutator untuk mengakses dan mengatur attributes ‘nomor_hp’.
Simpan class tersebut dengan nama karyawati.py
Buat file main.py yang mengimport class ‘Karyawan’ dan ‘Karyawati’
Di dalam main.py, create 2 objek yang berasal dari class ‘Karyawan’ dan ‘Karyawati’ dan isi parameter dan
set ‘nomor_hp’.
Print nama dan ‘nomor_hp’ dari kedua objek yang telah dibuat tadi
Upload PR ini ke dalam Google Classroom paling lambat Hari Rabu, Jam 23.59 WIB. Penalti kalau mengumpulkan PR lebih dari tenggat waktu yang telah ditentukan adalah nilai yang kosong (0).

Selamat mengerjakan teman-teman, dan good luck! : )

Harap perhatian :
-Nama diharapkan menggunakan nama asli
-Jika ada pertanyaan terkait homework dapat ditanyakan pada tutor melalui grup whatsapp kelas
Class comments
Your work
Graded

karyawan.py
Text

main.py
Text

karyawati.py
Text

homework 11-1.png
Image

__init__.py
Text
Private comments
# -*- coding: utf-8 -*-
"""Karyawan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hIqw9C_CIzUKaRI8sI87migu36MBwHdB
"""

class Karyawan:
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

karyawan.py
Displaying karyawan.py.