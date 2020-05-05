
# Sirepo-Development-Updates
this records the sirepo developments from NSLS-II

### 10, will do : add 'wm_fbk' to script...........

Before running a Sirepo-generated script of NERSC, you should add this option in it:

      ['wm_fbk', '', '1', 'create backup file(s) with propagated multi-e intensity distribution vs horizontal and vertical position and other radiation characteristics', 'store_true'],

By default, this option is not set in the srwl_bl.py file (see https://github.com/ochubar/SRW/blob/master/env/work/srw_python/srwl_bl.py#L3566). 

BTW, I am using now RadiaSoft's Sirepo version for direct simulations at NERSC, in the Debug queue. Great development! I have even prepared a happy slide on this for DOE (see slide #15 in the attached file).
Though this "'wm_fbk " option still has to be added in Sirepo and used there; maybe we can do this and make a pull request to RadiaSoft?.

### 9, the separate tab "Grid Shift" to the "Propagation Parameters" dialog
[example script](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/sxn_v02_250ev_realzp-debug-intensity-watchpoint-56753227m_oc.py)
### ![grid shift](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/propagator_gridshift.PNG)


### 8, the modification of official beamline logo in light-source page
```
https://expdev-test.nsls2.bnl.gov/light#/light-sources
```
### ![light-sources](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/light-sources.PNG)

### 7, "demo videos" is ready to be added
### ![demo_video](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/demo_video.PNG)
[demo_note](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/video-audio-template.txt)

### 6, disable "user register".

### 5, 3D beamline plot generation without wavefront propagation calculation is done.

### 4, fixed the issue with initial conditions for e- trajectory for all examples.

### 3, fixed some issue in the field of 'degree of coherence'.
The correct values should be ‘Manual’ and ‘-1.8’.
### ![ebeam_initial](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/ebeam_initial.PNG)

### 2, For grating, there are following updating:
* add “Compute Parameters from”, then when input ‘energy’ and ‘cff’ (or ‘grazing angle’), it will automatically calculate ‘grazing angle’ (or ‘cff’).
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Heigh Profile' to grating field.

### 1, For crystal, there are following updating:
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Heigh Profile' to grating field.
