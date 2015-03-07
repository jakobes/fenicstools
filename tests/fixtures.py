from dolfin import *
import pytest

fixture = pytest.fixture(scope="module")

@fixture
def mesh_2D():
    return UnitSquareMesh(4, 4)

@fixture
def mesh_3D():
    return UnitCubeMesh(4, 4, 4)

@fixture
def V2(mesh_2D):
    return FunctionSpace(mesh_2D, 'CG', 1)

@fixture
def V3(mesh_3D):
    return FunctionSpace(mesh_3D, 'CG', 1)

@fixture
def VF2(mesh_2D):
    return VectorFunctionSpace(mesh_2D, "CG", 1)

@fixture
def VF3(mesh_3D):
    return VectorFunctionSpace(mesh_3D, "CG", 1)
