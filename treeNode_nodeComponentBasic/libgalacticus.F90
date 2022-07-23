!! Copyright 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018,
!!           2019, 2020, 2021, 2022
!!    Andrew Benson <abenson@carnegiescience.edu>
!!
!! This file is part of Galacticus.
!!
!!    Galacticus is free software: you can redistribute it and/or modify
!!    it under the terms of the GNU General Public License as published by
!!    the Free Software Foundation, either version 3 of the License, or
!!    (at your option) any later version.
!!
!!    Galacticus is distributed in the hope that it will be useful,
!!    but WITHOUT ANY WARRANTY; without even the implied warranty of
!!    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
!!    GNU General Public License for more details.
!!
!!    You should have received a copy of the GNU General Public License
!!    along with Galacticus.  If not, see <http://www.gnu.org/licenses/>.

  !!{
  A wrapper file which simply includes the auto-generated content for {\normalfont \ttfamily libgalacticus}.
  !!}

include 'libgalacticus.inc'

!! TREE NODE IMPLEMENTATION
  
function treeNodeL(id) bind(c,name="treeNodeL")
  use :: Galacticus_Nodes, only : treeNode
  use :: Kind_Numbers, only : kind_int8
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_f_pointer
  implicit none
  type(c_ptr) :: treeNodeL
  integer(kind_int8), value :: id
  type(treeNode), pointer :: node
   
  node => treeNode(id)
  treeNodeL=c_loc(node)
return
end function treeNodeL

function treeNodeIDL(self) bind(c,name='treeNodeIDL')
  use            :: Galacticus_Nodes, only : treeNode ! Import the treeNode object.
  use, intrinsic :: ISO_C_Binding   , only : c_long, c_ptr, c_f_pointer
  implicit none
  integer(c_long  )          :: treeNodeIDL ! This will be the value we return to Python.
  type   (c_ptr   ), value   :: self        ! This is the raw pointer to the memory location containing the treeNode object.
  type   (treeNode), pointer :: self_       ! This is a Fortran pointer to a treeNode object.

  ! The 'c_f_pointer' function assigns the location of a C-style pointer ("self") to a Fortran object ("self_").
  call c_f_pointer(self,self_)
  ! Now we can call the Fortran function needed to get the ID number, and put it into our return variable.
  treeNodeIDL=self_%index()
  return
end function treeNodeIDL

subroutine treeNodeSetIDL(self, newID) bind(c,name='treeNodeSetIDL')
  use            :: Galacticus_Nodes, only : treeNode
  use, intrinsic :: ISO_C_Binding   , only : c_long, c_ptr, c_f_pointer
  use :: Kind_Numbers, only : kind_int8
  implicit none
  integer(c_long   ), value :: newID ! Declare C-compatible type of newID
  integer(kind_int8)        :: newID_
  type   (c_ptr   ), value   :: self  
  type   (treeNode), pointer :: self_  

  call c_f_pointer(self,self_)
  newID_=newID
  call self_%indexSet(newID_)
end subroutine treeNodeSetIDL

!! NODE COMPONENT IMPLEMENTATION

function nodeComponentBasicL(treeNodeL) bind(c, name='nodeComponentBasicL')
  use :: Galacticus_Nodes                , only : treeNode, nodeComponentBasic, nodeComponentBasicStandard
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_f_pointer
  implicit none

  class(nodeComponentBasic), pointer :: basic_
  type(nodecomponentBasicStandard), pointer :: basicStandard
  type   (c_ptr   ), value   :: treeNodeL
  type   (treeNode), pointer :: treeNodeL_
  type(c_ptr) :: nodeComponentBasicL

  call c_f_pointer(treeNodeL, treeNodeL_)
  basic_ => treeNodeL_%basic(autoCreate=.true.)

  select type(basic_)
  type is(nodecomponentBasicStandard)
    basicStandard => basic_
  end select

  nodeComponentBasicL=c_loc(basicStandard)
return
end function nodeComponentBasicL

function nodeComponentBasicMassL(self) bind(c, name='nodeComponentBasicMassL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic , nodecomponentBasicStandard
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_double, c_f_pointer
  implicit none

  type   (c_ptr   ), value :: self  
  type(nodecomponentBasicStandard), pointer :: self_
  real(c_double ) :: nodeComponentBasicMassL

  call c_f_pointer(self, self_)
  nodeComponentBasicMassL = self_%mass()
return
end function nodeComponentBasicMassL

function nodeComponentBasicTimeL(self) bind(c, name='nodeComponentBasicTimeL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic, nodeComponentBasicStandard 
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_double, c_f_pointer
  implicit none

  type   (c_ptr   ), value :: self  
  type(nodeComponentBasicStandard), pointer :: self_
  real(c_double ) :: nodeComponentBasicTimeL

  call c_f_pointer(self, self_)
  nodeComponentBasicTimeL = self_%time()
return
end function nodeComponentBasicTimeL

function nodeComponentBasicTimeLastIsolatedL(self) bind(c, name='nodeComponentBasicTimeLastIsolatedL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic, nodeComponentBasicStandard 
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_double, c_f_pointer
  implicit none

  type   (c_ptr   ), value :: self  
  type(nodeComponentBasicStandard), pointer :: self_
  real(c_double ) :: nodeComponentBasicTimeLastIsolatedL

  call c_f_pointer(self, self_)
  nodeComponentBasicTimeLastIsolatedL = self_%timeLastIsolated()
return
end function nodeComponentBasicTimeLastIsolatedL

subroutine nodeComponentBasicSetMassL(self, mass) bind(c, name='nodeComponentBasicSetMassL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic , nodeComponentBasicStandard 
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_double, c_f_pointer
  implicit none
  
  type   (c_ptr   ), value :: self  
  type(nodeComponentBasicStandard), pointer :: self_
  real(c_double   ), value :: mass 
  double precision :: mass_

  call c_f_pointer(self, self_)
  mass_=mass
  call self_%massSet(mass_)
end subroutine nodeComponentBasicSetMassL

subroutine nodeComponentBasicSetTimeL(self, time) bind(c, name='nodeComponentBasicSetTimeL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic , nodeComponentBasicStandard
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_f_pointer, c_double
  implicit none

  type   (c_ptr   ), value :: self  
  type(nodeComponentBasicStandard), pointer :: self_
  real(c_double   ), value :: time 
  double precision :: time_

  call c_f_pointer(self, self_)
  time_=time
  call self_%timeSet(time_)
end subroutine nodeComponentBasicSetTimeL

subroutine nodeComponentBasicSetTimeLastIsolatedL(self, timeLastIsolated) bind(c, name='nodeComponentBasicSetTimeLastIsolatedL')
  use :: Galacticus_Nodes                , only : nodeComponentBasic , nodeComponentBasicStandard
  use, intrinsic :: ISO_C_Binding, only : c_ptr, c_loc, c_f_pointer, c_double
  implicit none

  type   (c_ptr   ), value :: self  
  type(nodeComponentBasicStandard), pointer :: self_
  real(c_double   ), value :: timeLastIsolated 
  double precision :: timeLastIsolated_

  call c_f_pointer(self, self_)
  timeLastIsolated_ = timeLastIsolated
  call self_%timeLastIsolatedSet(timeLastIsolated_)
end subroutine nodeComponentBasicSetTimeLastIsolatedL
