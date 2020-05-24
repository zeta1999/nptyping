from unittest import TestCase

import numpy as np

from nptyping import (
    get_type,
    Int32,
    Float64,
    Int8,
    Int16,
    Int64,
    UInt8,
    UInt16,
    UInt32,
    UInt64,
    Float16,
    Float32,
)


class TestGetType(TestCase):

    def test_get_type_int(self):
        self.assertEqual(Int32, get_type(42))

    def test_get_type_float(self):
        self.assertEqual(Float64, get_type(42.0))

    def test_get_type_numpy_dtype(self):
        self.assertEqual(Int8, get_type(np.int8(42)))
        self.assertEqual(Int16, get_type(np.int16(42)))
        self.assertEqual(Int32, get_type(np.int32(42)))
        self.assertEqual(Int64, get_type(np.int64(42)))

        self.assertEqual(UInt8, get_type(np.uint8(42)))
        self.assertEqual(UInt16, get_type(np.uint16(42)))
        self.assertEqual(UInt32, get_type(np.uint32(42)))
        self.assertEqual(UInt64, get_type(np.uint64(42)))

        self.assertEqual(Float16, get_type(np.float16(42.0)))
        self.assertEqual(Float32, get_type(np.float32(42.0)))
        self.assertEqual(Float64, get_type(np.float64(42.0)))

    def test_get_type_numpy_type(self):
        self.assertEqual(Int8, get_type(np.int8))
        self.assertEqual(Int16, get_type(np.int16))
        self.assertEqual(Int32, get_type(np.int32))
        self.assertEqual(Int64, get_type(np.int64))

        self.assertEqual(UInt8, get_type(np.uint8))
        self.assertEqual(UInt16, get_type(np.uint16))
        self.assertEqual(UInt32, get_type(np.uint32))
        self.assertEqual(UInt64, get_type(np.uint64))

        self.assertEqual(Float16, get_type(np.float16))
        self.assertEqual(Float32, get_type(np.float32))
        self.assertEqual(Float64, get_type(np.float64))

    def test_get_type_not_understood(self):
        class SomeRandomClass:
            ...

        # Test invalid instances.
        with self.assertRaises(TypeError) as err:
            get_type(SomeRandomClass())
        self.assertIn(SomeRandomClass.__name__, str(err.exception))

        # Test invalid types.
        with self.assertRaises(TypeError) as err:
            get_type(SomeRandomClass)
        self.assertIn(SomeRandomClass.__name__, str(err.exception))
