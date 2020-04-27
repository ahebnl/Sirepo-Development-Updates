
# Sirepo-Development-Updates
this records the sirepo developments from NSLS-II
### 1, For crystal, there are following updating:
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Heigh Profile' to grating field.

### 2, For grating, there are following updating:
* add “Compute Parameters from”, then when input ‘energy’ and ‘cff’ (or ‘grazing angle’), it will automatically calculate ‘grazing angle’ (or ‘cff’).
* the orientation parameters will be updated synchronously with ‘grazing angle’
* the orientation parameters in propagator will be updated synchronously.
* add 'Heigh Profile' to grating field.

### 3, fixed some issue in the field of 'degree of coherence'.

### 4, fixed the issue with initial conditions for e- trajectory for all examples.
The correct values should be ‘Manual’ and ‘-1.8’.
### ![ebeam_initial](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/ebeam_initial.PNG)

### 5, 3D beamline plot generation without wavefront propagation calculation is done.
### 6, disable "user register".
### 7, "demo videos" is ready to be added
### ![demo_video](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/demo_video.PNG)
[demo_note](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/video-audio-template.txt)

### 8, the modification of official beamline logo in light-source page
```
http://10.10.10.11:8000/light#/light-sources
```
### ![light-sources](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/light-sources.PNG)

### 9, the separate tab "Grid Shift" to the "Propagation Parameters" dialog
[example script](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/sxn_v02_250ev_realzp-debug-intensity-watchpoint-56753227m_oc.py)
### ![grid shift](https://github.com/ahebnl/Sirepo-Development-Updates/blob/master/propagator_gridshift.PNG)
