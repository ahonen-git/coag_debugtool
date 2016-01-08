import os
import numpy as np
import numpy.ma as ma
import Ngl
import netCDF4
from pandas import Series, DataFrame
import pandas as pd
 
src_nc0 = netCDF4.Dataset('../data/coag_matlab.nc' ,'r')
src_nc1 = netCDF4.Dataset('../data/coag_fortran.nc','r')

b0_brown_b1  = src_nc0.variables["b_brown.b1"][:]
b1_brown_b1  = src_nc1.variables["b_brown.b1"][:]
b0_brown_b2  = src_nc0.variables["b_brown.b2"][:]
b1_brown_b2  = src_nc1.variables["b_brown.b2"][:]
b0_brown_b3  = src_nc0.variables["b_brown.b3"][:]
b1_brown_b3  = src_nc1.variables["b_brown.b3"][:]
b0_brown_b4  = src_nc0.variables["b_brown.b4"][:]
b1_brown_b4  = src_nc1.variables["b_brown.b4"][:]
b0_brown_b5  = src_nc0.variables["b_brown.b5"][:]
b1_brown_b5  = src_nc1.variables["b_brown.b5"][:]
b0_brown_b25 = src_nc0.variables["b_brown.b25"][:]
b1_brown_b25 = src_nc1.variables["b_brown.b25"][:]

b0_shear_b1 = src_nc0.variables["b_shear.b1"][:]
b1_shear_b1 = src_nc1.variables["b_shear.b1"][:]
b0_shear_b2 = src_nc0.variables["b_shear.b2"][:]
b1_shear_b2 = src_nc1.variables["b_shear.b2"][:]
b0_shear_b3 = src_nc0.variables["b_shear.b3"][:]
b1_shear_b3 = src_nc1.variables["b_shear.b3"][:]
b0_shear_b4 = src_nc0.variables["b_shear.b4"][:]
b1_shear_b4 = src_nc1.variables["b_shear.b4"][:]
b0_shear_b5 = src_nc0.variables["b_shear.b5"][:]
b1_shear_b5 = src_nc1.variables["b_shear.b5"][:]
b0_shear_b25 = src_nc0.variables["b_shear.b25"][:]
b1_shear_b25 = src_nc1.variables["b_shear.b25"][:]

b0_ds_b1  = src_nc0.variables["b_ds.b1"][:]
b1_ds_b1  = src_nc1.variables["b_ds.b1"][:]
b0_ds_b2  = src_nc0.variables["b_ds.b2"][:]
b1_ds_b2  = src_nc1.variables["b_ds.b2"][:]
b0_ds_b3  = src_nc0.variables["b_ds.b3"][:]
b1_ds_b3  = src_nc1.variables["b_ds.b3"][:]
b0_ds_b4  = src_nc0.variables["b_ds.b4"][:]
b1_ds_b4  = src_nc1.variables["b_ds.b4"][:]
b0_ds_b5  = src_nc0.variables["b_ds.b5"][:]
b1_ds_b5  = src_nc1.variables["b_ds.b5"][:]
b0_ds_b25 = src_nc0.variables["b_ds.b25"][:]
b1_ds_b25 = src_nc1.variables["b_ds.b25"][:]

src_nc0.close()
src_nc1.close()

x = arange(47)
y = arange(47)
y = y[::-1]

X, Y = meshgrid(x, y)

z_brown_b1  = (b1_brown_b1  - b0_brown_b1) /b0_brown_b1  * 100.0
z_brown_b2  = (b1_brown_b2  - b0_brown_b2) /b0_brown_b2  * 100.0
z_brown_b3  = (b1_brown_b3  - b0_brown_b3) /b0_brown_b3  * 100.0
z_brown_b4  = (b1_brown_b4  - b0_brown_b4) /b0_brown_b4  * 100.0
z_brown_b5  = (b1_brown_b5  - b0_brown_b5) /b0_brown_b5  * 100.0
z_brown_b25 = (b1_brown_b25 - b0_brown_b25)/b0_brown_b25 * 100.0

z_shear_b1  = (b1_shear_b1  - b0_shear_b1)/b0_shear_b1   * 100.0
z_shear_b2  = (b1_shear_b2  - b0_shear_b2)/b0_shear_b2   * 100.0
z_shear_b3  = (b1_shear_b3  - b0_shear_b3)/b0_shear_b3   * 100.0
z_shear_b4  = (b1_shear_b4  - b0_shear_b4)/b0_shear_b4   * 100.0
z_shear_b5  = (b1_shear_b5  - b0_shear_b5)/b0_shear_b5   * 100.0
z_shear_b25 = (b1_shear_b25 - b0_shear_b25)/b0_shear_b25 * 100.0

z_ds_b1  = (b1_ds_b1  - b0_ds_b1) /b0_ds_b1  * 100.0
z_ds_b2  = (b1_ds_b2  - b0_ds_b2) /b0_ds_b2  * 100.0
z_ds_b3  = (b1_ds_b3  - b0_ds_b3) /b0_ds_b3  * 100.0
z_ds_b4  = (b1_ds_b4  - b0_ds_b4) /b0_ds_b4  * 100.0
z_ds_b5  = (b1_ds_b5  - b0_ds_b5) /b0_ds_b5  * 100.0
z_ds_b25 = (b1_ds_b25 - b0_ds_b25)/b0_ds_b25 * 100.0

z_brown_b1  = ma.masked_where(np.isnan(z_brown_b1) ,z_brown_b1 )
z_brown_b2  = ma.masked_where(np.isnan(z_brown_b2) ,z_brown_b2 )
z_brown_b3  = ma.masked_where(np.isnan(z_brown_b3) ,z_brown_b3 )
z_brown_b4  = ma.masked_where(np.isnan(z_brown_b4) ,z_brown_b4 )
z_brown_b5  = ma.masked_where(np.isnan(z_brown_b5) ,z_brown_b5 )
z_brown_b25 = ma.masked_where(np.isnan(z_brown_b25),z_brown_b25)

z_shear_b1  = ma.masked_where(np.isnan(z_shear_b1) ,z_shear_b1 )
z_shear_b2  = ma.masked_where(np.isnan(z_shear_b2) ,z_shear_b2 )
z_shear_b3  = ma.masked_where(np.isnan(z_shear_b3) ,z_shear_b3 )
z_shear_b4  = ma.masked_where(np.isnan(z_shear_b4) ,z_shear_b4 )
z_shear_b5  = ma.masked_where(np.isnan(z_shear_b5) ,z_shear_b5 )
z_shear_b25 = ma.masked_where(np.isnan(z_shear_b25),z_shear_b25)

z_ds_b1  = ma.masked_where(np.isnan(z_ds_b1) ,z_ds_b1 )
z_ds_b2  = ma.masked_where(np.isnan(z_ds_b2) ,z_ds_b2 )
z_ds_b3  = ma.masked_where(np.isnan(z_ds_b3) ,z_ds_b3 )
z_ds_b4  = ma.masked_where(np.isnan(z_ds_b4) ,z_ds_b4 )
z_ds_b5  = ma.masked_where(np.isnan(z_ds_b5) ,z_ds_b5 )
z_ds_b25 = ma.masked_where(np.isnan(z_ds_b25),z_ds_b25)

fig0 = plt.figure()
fig1 = plt.figure()
fig2 = plt.figure()

ax0 = fig0.add_subplot(231)
ax1 = fig0.add_subplot(232)
ax2 = fig0.add_subplot(233)
ax3 = fig0.add_subplot(234)
ax4 = fig0.add_subplot(235)
ax5 = fig0.add_subplot(236)

bx0 = fig1.add_subplot(231)
bx1 = fig1.add_subplot(232)
bx2 = fig1.add_subplot(233)
bx3 = fig1.add_subplot(234)
bx4 = fig1.add_subplot(235)
bx5 = fig1.add_subplot(236)

cx0 = fig2.add_subplot(231)
cx1 = fig2.add_subplot(232)
cx2 = fig2.add_subplot(233)
cx3 = fig2.add_subplot(234)
cx4 = fig2.add_subplot(235)
cx5 = fig2.add_subplot(236)

ax0.set_xlim(0,46)
ax0.set_ylim(0,46)
ax1.set_xlim(0,46)
ax1.set_ylim(0,46)
ax2.set_xlim(0,46)
ax2.set_ylim(0,46)
ax3.set_xlim(0,46)
ax3.set_ylim(0,46)
ax4.set_xlim(0,46)
ax4.set_ylim(0,46)
ax5.set_xlim(0,46)
ax5.set_ylim(0,46)

bx0.set_xlim(0,46)
bx0.set_ylim(0,46)
bx1.set_xlim(0,46)
bx1.set_ylim(0,46)
bx2.set_xlim(0,46)
bx2.set_ylim(0,46)
bx3.set_xlim(0,46)
bx3.set_ylim(0,46)
bx4.set_xlim(0,46)
bx4.set_ylim(0,46)
bx5.set_xlim(0,46)
bx5.set_ylim(0,46)

cx0.set_xlim(0,46)
cx0.set_ylim(0,46)
cx1.set_xlim(0,46)
cx1.set_ylim(0,46)
cx2.set_xlim(0,46)
cx2.set_ylim(0,46)
cx3.set_xlim(0,46)
cx3.set_ylim(0,46)
cx4.set_xlim(0,46)
cx4.set_ylim(0,46)
cx5.set_xlim(0,46)
cx5.set_ylim(0,46)

cn0 = ax0.pcolormesh(X,Y,z_brown_b1 , vmin=-1.0,vmax=1.0, cmap='RdBu')
cn1 = ax1.pcolormesh(X,Y,z_brown_b2 , vmin=-1.0,vmax=1.0, cmap='RdBu')
cn2 = ax2.pcolormesh(X,Y,z_brown_b3 , vmin=-1.0,vmax=1.0, cmap='RdBu')
cn3 = ax3.pcolormesh(X,Y,z_brown_b4 , vmin=-1.0,vmax=1.0, cmap='RdBu')
cn4 = ax4.pcolormesh(X,Y,z_brown_b5 , vmin=-1.0,vmax=1.0, cmap='RdBu')
cn5 = ax5.pcolormesh(X,Y,z_brown_b25, vmin=-1.0,vmax=1.0, cmap='RdBu')

dn0 = bx0.pcolormesh(X,Y,z_shear_b1 , vmin=-1.0,vmax=1.0, cmap='RdBu')
dn1 = bx1.pcolormesh(X,Y,z_shear_b2 , vmin=-1.0,vmax=1.0, cmap='RdBu')
dn2 = bx2.pcolormesh(X,Y,z_shear_b3 , vmin=-1.0,vmax=1.0, cmap='RdBu')
dn3 = bx3.pcolormesh(X,Y,z_shear_b4 , vmin=-1.0,vmax=1.0, cmap='RdBu')
dn4 = bx4.pcolormesh(X,Y,z_shear_b5 , vmin=-1.0,vmax=1.0, cmap='RdBu')
dn5 = bx5.pcolormesh(X,Y,z_shear_b25, vmin=-1.0,vmax=1.0, cmap='RdBu')

en0 = cx0.pcolormesh(X,Y,z_ds_b1 , vmin=-1.0,vmax=1.0, cmap='RdBu')
en1 = cx1.pcolormesh(X,Y,z_ds_b2 , vmin=-1.0,vmax=1.0, cmap='RdBu')
en2 = cx2.pcolormesh(X,Y,z_ds_b3 , vmin=-1.0,vmax=1.0, cmap='RdBu')
en3 = cx3.pcolormesh(X,Y,z_ds_b4 , vmin=-1.0,vmax=1.0, cmap='RdBu')
en4 = cx4.pcolormesh(X,Y,z_ds_b5 , vmin=-1.0,vmax=1.0, cmap='RdBu')
en5 = cx5.pcolormesh(X,Y,z_ds_b25, vmin=-1.0,vmax=1.0, cmap='RdBu')

fig0.colorbar(cn0,ax=ax0)
fig0.colorbar(cn1,ax=ax1)
fig0.colorbar(cn2,ax=ax2)
fig0.colorbar(cn3,ax=ax3)
fig0.colorbar(cn4,ax=ax4)
fig0.colorbar(cn5,ax=ax5)

fig1.colorbar(dn0,ax=bx0)
fig1.colorbar(dn1,ax=bx1)
fig1.colorbar(dn2,ax=bx2)
fig1.colorbar(dn3,ax=bx3)
fig1.colorbar(dn4,ax=bx4)
fig1.colorbar(dn5,ax=bx5)

fig2.colorbar(en0,ax=cx0)
fig2.colorbar(en1,ax=cx1)
fig2.colorbar(en2,ax=cx2)
fig2.colorbar(en3,ax=cx3)
fig2.colorbar(en4,ax=cx4)
fig2.colorbar(en5,ax=cx5)

#dst_nc0 = netCDF4.Dataset('dstfile','a')
#src_nc0.close()
#dst_nc0.close()
#
###### print format #####
##print "%4.0f %4.0f -> %4.0f %4.0f" % (pstr, pend, rstr, rend)
#
###### get data #####
##dep   = ma.ravel(src_nc0.variables["z_t"]) * 1.e-2
##lat   = ma.ravel(src_nc0.variables["TLAT"][:,:])
##lon   = ma.ravel(src_nc0.variables["TLONG"][:,:])
##var3d = ma.copy (src_nc0.variables["Fe"][0,:,:,:]) * 1.e3
#
###### check abnormal data #####
##x = var3d
##x[x ==  np.inf] = var3d.fill_value  # eliminate inf values
##x[x == -np.inf] = var3d.fill_value
##x = ma.masked_outside(x,0.0,2.0)    # eliminate data outside the bound
##x = ma.compressed(x)                # eliminate masked data and compressed in an array
#
##print DataFrame(x).describe()
##plt.hist(x,50,histtype='bar')
##print DataFrame(dep)
#
###### draw by matplotlib #####
##fig0 = plt.figure()
##
##subplots_adjust(wspace=0.05)
##ax0 = fig0.add_subplot(131)
##ax1 = fig0.add_subplot(132,sharey=ax0)
##ax2 = fig0.add_subplot(133,sharey=ax0)
##
##ax0.grid(True)
##ax1.grid(True)
##ax2.grid(True)
##
##ax0.set_xlim(0.0, 3.5)
##ax1.set_xlim(0.0,50.0)
##ax2.set_xlim(0.0, 1.0)
##
##ax0.set_xticks(arange(0.0, 3.5, 0.5))
##ax1.set_xticks(arange(0.0,60.0,10.0))
##ax2.set_xticks(arange(0.0, 1.0, 0.2))
##
##plt.setp( ax1.get_yticklabels(), visible=False )
##plt.setp( ax2.get_yticklabels(), visible=False )
##
##ax0.set_xlabel("PO4 [uM]")
##ax0.set_ylabel("Depth [m]")
##ax1.set_xlabel("NO3 [uM]")
##ax2.set_xlabel("Fe  [nM]")
##
##ax0.plot(po4_0_z_a,z,color="black",label="POP" ,linewidth=2)
##ax0.plot(po4_1_z_a,z,color="red"  ,label="ROMS",linewidth=2)
##ax1.plot(no3_0_z_a,z,color="black",linewidth=2)
##ax1.plot(no3_1_z_a,z,color="red"  ,linewidth=2)
##ax2.plot(fe_0_z_a ,z,color="black",linewidth=2)
##ax2.plot(fe_1_z_a ,z,color="red"  ,linewidth=2)
##
##ax0.legend(loc="lower left")
#
##fig0.savefig('../psfiles/hogehoge.png',dpi=200)
#
#
#
###### draw by pyngl #####
##wks = Ngl.open_wks("ps",psf)
##
##res0 = Ngl.Resources()
##
##res0.nglDraw               = False
##res0.nglFrame              = False
##
##plot = []
##
##res0.sfYArray = lat
##res0.sfXArray = lon
##
##res0.cnFillOn              = True
##res0.cnFillMode            = "RasterFill"
##res0.cnLinesOn             = False
##res0.cnLineLabelsOn        = False
##
##res0.cnLevelSelectionMode  = "ManualLevels"
##res0.cnMinLevelValF        = 0.0
##res0.cnMaxLevelValF        = 2.0
##res0.cnLevelSpacingF       = 0.1
##
##res0.mpGridAndLimbOn       = False
##res0.mpCenterLonF          = -150
##
##res0.pmLabelBarDisplayMode = "Never"
##
##res0.lbLabelAutoStride     = True
##
##resT = Ngl.Resources()
##resT.txFontHeightF         = 0.02
##Ngl.text_ndc(wks,ttl,0.5,0.9,resT)
##
##for k in [0, 10, 26, 39]:
##  res0.tiMainString = str(dep[k]) + "m depth"
##  var = ma.ravel(var3d[k,:,:])
##  plot.append(Ngl.contour_map(wks,var,res0))
##
##
##resP = Ngl.Resources()
##resP.nglPanelLabelBar                 = True
##resP.nglPanelLabelBarLabelFontHeightF = 0.01
##resP.nglPanelLabelBarHeightF          = 0.10
##resP.nglPanelLabelBarWidthF           = 1.000
###resP.nglPanelFigureStrings            = ["a", "b", "c", "d"]
###resP.nglPanelFigureStringsJust        = "BottomRight"
##
##Ngl.panel(wks,plot[0:4],[2,2],resP)
#
###### output data into a netcdf file #####
##x = np.random.rand(1*60*116*110)
##x = x.reshape([1,60,116,100])
##dst_nc0.variables['TEMP'][:] = x[:]
## 
#
###### example of a cdl file. ##### 
##
## % ncgen -o hoge.nc hoge.cdl
##
######
##netcdf sample data {
##dimensions:
##        time = UNLIMITED ; // (1 currently)
##        z_t = 60 ;
##        nlon = 100 ;
##        nlat = 116 ;
##variables:
##        float TEMP(time, z_t, nlat, nlon) ;
##                TEMP:long_name = "Potential Temperature" ;
##                TEMP:units = "degC" ;
##                TEMP:coordinates = "TLONG TLAT z_t time" ;
##                TEMP:grid_loc = "3111" ;
##                TEMP:cell_methods = "time: mean" ;
##                TEMP:_FillValue = 9.96921e+36f ;
##                TEMP:missing_value = 9.96921e+36f ;
##
##// global attributes:
##                :title = "c.e13.CECO.T62_g37.INX.001" ;
##}
#
#
###### read fortran binary #####
##temp=np.fromfile('temp.bin',dtype='>f8',count=60*116*100)  # '>' represents big endian
##temp = a.reshape((60,116,100))

#b0_ds_b1 = src_nc0.variables["b_ds.b1"][:]
#b1_ds_b1 = src_nc1.variables["b_ds.b1"][:]
#b0_ds_b2 = src_nc0.variables["b_ds.b2"][:]
#b1_ds_b2 = src_nc1.variables["b_ds.b2"][:]
#b0_ds_b3 = src_nc0.variables["b_ds.b3"][:]
#b1_ds_b3 = src_nc1.variables["b_ds.b3"][:]
#b0_ds_b4 = src_nc0.variables["b_ds.b4"][:]
#b1_ds_b4 = src_nc1.variables["b_ds.b4"][:]
#b0_ds_b5 = src_nc0.variables["b_ds.b5"][:]
#b1_ds_b5 = src_nc1.variables["b_ds.b5"][:]
#
#src_nc0.close()
#src_nc1.close()
#
#x = arange(47)
#y = arange(47)
#y = y[::-1]
#
#X, Y = meshgrid(x, y)
#
#z_brown_b1 = (b1_brown_b1 - b0_brown_b1)/b0_brown_b1 * 100.0
#z_brown_b2 = (b1_brown_b2 - b0_brown_b2)/b0_brown_b2 * 100.0
#z_brown_b3 = (b1_brown_b3 - b0_brown_b3)/b0_brown_b3 * 100.0
#z_brown_b4 = (b1_brown_b4 - b0_brown_b4)/b0_brown_b4 * 100.0
#z_brown_b5 = (b1_brown_b5 - b0_brown_b5)/b0_brown_b5 * 100.0
#
#z_shear_b1 = (b1_shear_b1 - b0_shear_b1)/b0_shear_b1 * 100.0
#z_shear_b2 = (b1_shear_b2 - b0_shear_b2)/b0_shear_b2 * 100.0
#z_shear_b3 = (b1_shear_b3 - b0_shear_b3)/b0_shear_b3 * 100.0
#z_shear_b4 = (b1_shear_b4 - b0_shear_b4)/b0_shear_b4 * 100.0
#z_shear_b5 = (b1_shear_b5 - b0_shear_b5)/b0_shear_b5 * 100.0
#
#z_ds_b1 = (b1_ds_b1 - b0_ds_b1)/b0_ds_b1 * 100.0
#z_ds_b2 = (b1_ds_b2 - b0_ds_b2)/b0_ds_b2 * 100.0
#z_ds_b3 = (b1_ds_b3 - b0_ds_b3)/b0_ds_b3 * 100.0
#z_ds_b4 = (b1_ds_b4 - b0_ds_b4)/b0_ds_b4 * 100.0
#z_ds_b5 = (b1_ds_b5 - b0_ds_b5)/b0_ds_b5 * 100.0
#
#z_brown_b1 = ma.masked_where(np.isnan(z_brown_b1),z_brown_b1)
#z_brown_b2 = ma.masked_where(np.isnan(z_brown_b2),z_brown_b2)
#z_brown_b3 = ma.masked_where(np.isnan(z_brown_b3),z_brown_b3)
#z_brown_b4 = ma.masked_where(np.isnan(z_brown_b4),z_brown_b4)
#z_brown_b5 = ma.masked_where(np.isnan(z_brown_b5),z_brown_b5)
#
#z_shear_b1 = ma.masked_where(np.isnan(z_shear_b1),z_shear_b1)
#z_shear_b2 = ma.masked_where(np.isnan(z_shear_b2),z_shear_b2)
#z_shear_b3 = ma.masked_where(np.isnan(z_shear_b3),z_shear_b3)
#z_shear_b4 = ma.masked_where(np.isnan(z_shear_b4),z_shear_b4)
#z_shear_b5 = ma.masked_where(np.isnan(z_shear_b5),z_shear_b5)
#
#z_ds_b1 = ma.masked_where(np.isnan(z_ds_b1),z_ds_b1)
#z_ds_b2 = ma.masked_where(np.isnan(z_ds_b2),z_ds_b2)
#z_ds_b3 = ma.masked_where(np.isnan(z_ds_b3),z_ds_b3)
#z_ds_b4 = ma.masked_where(np.isnan(z_ds_b4),z_ds_b4)
#z_ds_b5 = ma.masked_where(np.isnan(z_ds_b5),z_ds_b5)
#
#fig0 = plt.figure()
#fig1 = plt.figure()
#fig2 = plt.figure()
#
#ax0 = fig0.add_subplot(231)
#ax1 = fig0.add_subplot(232)
#ax2 = fig0.add_subplot(233)
#ax3 = fig0.add_subplot(234)
#ax4 = fig0.add_subplot(235)
#
#bx0 = fig1.add_subplot(231)
#bx1 = fig1.add_subplot(232)
#bx2 = fig1.add_subplot(233)
#bx3 = fig1.add_subplot(234)
#bx4 = fig1.add_subplot(235)
#
#cx0 = fig2.add_subplot(231)
#cx1 = fig2.add_subplot(232)
#cx2 = fig2.add_subplot(233)
#cx3 = fig2.add_subplot(234)
#cx4 = fig2.add_subplot(235)
#
#ax0.set_xlim(0,46)
#ax0.set_ylim(0,46)
#ax1.set_xlim(0,46)
#ax1.set_ylim(0,46)
#ax2.set_xlim(0,46)
#ax2.set_ylim(0,46)
#ax3.set_xlim(0,46)
#ax3.set_ylim(0,46)
#ax4.set_xlim(0,46)
#ax4.set_ylim(0,46)
#
#bx0.set_xlim(0,46)
#bx0.set_ylim(0,46)
#bx1.set_xlim(0,46)
#bx1.set_ylim(0,46)
#bx2.set_xlim(0,46)
#bx2.set_ylim(0,46)
#bx3.set_xlim(0,46)
#bx3.set_ylim(0,46)
#bx4.set_xlim(0,46)
#bx4.set_ylim(0,46)
#
#cx0.set_xlim(0,46)
#cx0.set_ylim(0,46)
#cx1.set_xlim(0,46)
#cx1.set_ylim(0,46)
#cx2.set_xlim(0,46)
#cx2.set_ylim(0,46)
#cx3.set_xlim(0,46)
#cx3.set_ylim(0,46)
#cx4.set_xlim(0,46)
#cx4.set_ylim(0,46)
#
#cn0 = ax0.pcolormesh(X,Y,z_brown_b1, vmin=-10.0,vmax=10.0, cmap='RdBu')
#cn1 = ax1.pcolormesh(X,Y,z_brown_b2, vmin=-10.0,vmax=10.0, cmap='RdBu')
#cn2 = ax2.pcolormesh(X,Y,z_brown_b3, vmin=-10.0,vmax=10.0, cmap='RdBu')
#cn3 = ax3.pcolormesh(X,Y,z_brown_b4, vmin=-10.0,vmax=10.0, cmap='RdBu')
#cn4 = ax4.pcolormesh(X,Y,z_brown_b5, vmin=-10.0,vmax=10.0, cmap='RdBu')
#
#dn0 = bx0.pcolormesh(X,Y,z_shear_b1, vmin=-10.0,vmax=10.0, cmap='RdBu')
#dn1 = bx1.pcolormesh(X,Y,z_shear_b2, vmin=-10.0,vmax=10.0, cmap='RdBu')
#dn2 = bx2.pcolormesh(X,Y,z_shear_b3, vmin=-10.0,vmax=10.0, cmap='RdBu')
#dn3 = bx3.pcolormesh(X,Y,z_shear_b4, vmin=-10.0,vmax=10.0, cmap='RdBu')
#dn4 = bx4.pcolormesh(X,Y,z_shear_b5, vmin=-10.0,vmax=10.0, cmap='RdBu')
#
#en0 = cx0.pcolormesh(X,Y,z_ds_b1, vmin=-10.0,vmax=10.0, cmap='RdBu')
#en1 = cx1.pcolormesh(X,Y,z_ds_b2, vmin=-10.0,vmax=10.0, cmap='RdBu')
#en2 = cx2.pcolormesh(X,Y,z_ds_b3, vmin=-10.0,vmax=10.0, cmap='RdBu')
#en3 = cx3.pcolormesh(X,Y,z_ds_b4, vmin=-10.0,vmax=10.0, cmap='RdBu')
#en4 = cx4.pcolormesh(X,Y,z_ds_b5, vmin=-10.0,vmax=10.0, cmap='RdBu')
#
#fig0.colorbar(cn0,ax=ax0)
#fig0.colorbar(cn1,ax=ax1)
#fig0.colorbar(cn2,ax=ax2)
#fig0.colorbar(cn3,ax=ax3)
#fig0.colorbar(cn4,ax=ax4)
#
#fig1.colorbar(dn0,ax=bx0)
#fig1.colorbar(dn1,ax=bx1)
#fig1.colorbar(dn2,ax=bx2)
#fig1.colorbar(dn3,ax=bx3)
#fig1.colorbar(dn4,ax=bx4)
#
#fig2.colorbar(en0,ax=cx0)
#fig2.colorbar(en1,ax=cx1)
#fig2.colorbar(en2,ax=cx2)
#fig2.colorbar(en3,ax=cx3)
#fig2.colorbar(en4,ax=cx4)
#
#
#
##dst_nc0 = netCDF4.Dataset('dstfile','a')
##src_nc0.close()
##dst_nc0.close()
##
####### print format #####
###print "%4.0f %4.0f -> %4.0f %4.0f" % (pstr, pend, rstr, rend)
##
####### get data #####
###dep   = ma.ravel(src_nc0.variables["z_t"]) * 1.e-2
###lat   = ma.ravel(src_nc0.variables["TLAT"][:,:])
###lon   = ma.ravel(src_nc0.variables["TLONG"][:,:])
###var3d = ma.copy (src_nc0.variables["Fe"][0,:,:,:]) * 1.e3
##
####### check abnormal data #####
###x = var3d
###x[x ==  np.inf] = var3d.fill_value  # eliminate inf values
###x[x == -np.inf] = var3d.fill_value
###x = ma.masked_outside(x,0.0,2.0)    # eliminate data outside the bound
###x = ma.compressed(x)                # eliminate masked data and compressed in an array
##
###print DataFrame(x).describe()
###plt.hist(x,50,histtype='bar')
###print DataFrame(dep)
##
####### draw by matplotlib #####
###fig0 = plt.figure()
###
###subplots_adjust(wspace=0.05)
###ax0 = fig0.add_subplot(131)
###ax1 = fig0.add_subplot(132,sharey=ax0)
###ax2 = fig0.add_subplot(133,sharey=ax0)
###
###ax0.grid(True)
###ax1.grid(True)
###ax2.grid(True)
###
###ax0.set_xlim(0.0, 3.5)
###ax1.set_xlim(0.0,50.0)
###ax2.set_xlim(0.0, 1.0)
###
###ax0.set_xticks(arange(0.0, 3.5, 0.5))
###ax1.set_xticks(arange(0.0,60.0,10.0))
###ax2.set_xticks(arange(0.0, 1.0, 0.2))
###
###plt.setp( ax1.get_yticklabels(), visible=False )
###plt.setp( ax2.get_yticklabels(), visible=False )
###
###ax0.set_xlabel("PO4 [uM]")
###ax0.set_ylabel("Depth [m]")
###ax1.set_xlabel("NO3 [uM]")
###ax2.set_xlabel("Fe  [nM]")
###
###ax0.plot(po4_0_z_a,z,color="black",label="POP" ,linewidth=2)
###ax0.plot(po4_1_z_a,z,color="red"  ,label="ROMS",linewidth=2)
###ax1.plot(no3_0_z_a,z,color="black",linewidth=2)
###ax1.plot(no3_1_z_a,z,color="red"  ,linewidth=2)
###ax2.plot(fe_0_z_a ,z,color="black",linewidth=2)
###ax2.plot(fe_1_z_a ,z,color="red"  ,linewidth=2)
###
###ax0.legend(loc="lower left")
##
###fig0.savefig('../psfiles/hogehoge.png',dpi=200)
##
##
##
####### draw by pyngl #####
###wks = Ngl.open_wks("ps",psf)
###
###res0 = Ngl.Resources()
###
###res0.nglDraw               = False
###res0.nglFrame              = False
###
###plot = []
###
###res0.sfYArray = lat
###res0.sfXArray = lon
###
###res0.cnFillOn              = True
###res0.cnFillMode            = "RasterFill"
###res0.cnLinesOn             = False
###res0.cnLineLabelsOn        = False
###
###res0.cnLevelSelectionMode  = "ManualLevels"
###res0.cnMinLevelValF        = 0.0
###res0.cnMaxLevelValF        = 2.0
###res0.cnLevelSpacingF       = 0.1
###
###res0.mpGridAndLimbOn       = False
###res0.mpCenterLonF          = -150
###
###res0.pmLabelBarDisplayMode = "Never"
###
###res0.lbLabelAutoStride     = True
###
###resT = Ngl.Resources()
###resT.txFontHeightF         = 0.02
###Ngl.text_ndc(wks,ttl,0.5,0.9,resT)
###
###for k in [0, 10, 26, 39]:
###  res0.tiMainString = str(dep[k]) + "m depth"
###  var = ma.ravel(var3d[k,:,:])
###  plot.append(Ngl.contour_map(wks,var,res0))
###
###
###resP = Ngl.Resources()
###resP.nglPanelLabelBar                 = True
###resP.nglPanelLabelBarLabelFontHeightF = 0.01
###resP.nglPanelLabelBarHeightF          = 0.10
###resP.nglPanelLabelBarWidthF           = 1.000
####resP.nglPanelFigureStrings            = ["a", "b", "c", "d"]
####resP.nglPanelFigureStringsJust        = "BottomRight"
###
###Ngl.panel(wks,plot[0:4],[2,2],resP)
##
####### output data into a netcdf file #####
###x = np.random.rand(1*60*116*110)
###x = x.reshape([1,60,116,100])
###dst_nc0.variables['TEMP'][:] = x[:]
### 
##
####### example of a cdl file. ##### 
###
### % ncgen -o hoge.nc hoge.cdl
###
#######
###netcdf sample data {
###dimensions:
###        time = UNLIMITED ; // (1 currently)
###        z_t = 60 ;
###        nlon = 100 ;
###        nlat = 116 ;
###variables:
###        float TEMP(time, z_t, nlat, nlon) ;
###                TEMP:long_name = "Potential Temperature" ;
###                TEMP:units = "degC" ;
###                TEMP:coordinates = "TLONG TLAT z_t time" ;
###                TEMP:grid_loc = "3111" ;
###                TEMP:cell_methods = "time: mean" ;
###                TEMP:_FillValue = 9.96921e+36f ;
###                TEMP:missing_value = 9.96921e+36f ;
###
###// global attributes:
###                :title = "c.e13.CECO.T62_g37.INX.001" ;
###}
##
##
####### read fortran binary #####
###temp=np.fromfile('temp.bin',dtype='>f8',count=60*116*100)  # '>' represents big endian
###temp = a.reshape((60,116,100))
##
####### write fortran binary #####
###temp_d[:] = temp[:]
###temp_d.byteswap(True) # convert little to big endian
###for nday in range(1,366):
###  ddd = "%03i" % nday
###  temp_d[nday-1,:,:,:].tofile('data/c.e13.C1DECO.T62_g37.INX.005.pop.TEMP.nday.0031.ieeer8.0001.'+ddd+'.12')
##
