#!/usr/bin/env python
import os
try:
    __IPYTHON__
    import sys
    del sys.argv[1:]
except:
    pass


import srwl_bl
import srwlib
import srwlpy
import srwl_uti_smp


def set_optics(v=None):
    el = []
    pp = []
    names = ['Fixed_Mask', 'Fixed_Mask_Ap_M1', 'Ap_M1', 'M1', 'M1_M2', 'M2', 'M2_Before_Grating', 'Before_Grating', 'Grating', 'Gr_Surf_Height_Err_Before_M3', 'Before_M3', 'M3', 'Lens_Before_Exit_Slit', 'Before_Exit_Slit', 'Exit_Slit', 'After_Exit_Slit', 'After_Exit_Slit_Before_ZP', 'Before_ZP', 'Ap_ZP', 'Zone_Plate', 'After_ZP', 'After_ZP_Watchpoint', 'Watchpoint']
    for el_name in names:
        if el_name == 'Fixed_Mask':
            # Fixed_Mask: aperture 20.0m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Fixed_Mask_shape,
                _ap_or_ob='a',
                _Dx=v.op_Fixed_Mask_Dx,
                _Dy=v.op_Fixed_Mask_Dy,
                _x=v.op_Fixed_Mask_x,
                _y=v.op_Fixed_Mask_y,
            ))
            pp.append(v.op_Fixed_Mask_pp)
        elif el_name == 'Fixed_Mask_Ap_M1':
            # Fixed_Mask_Ap_M1: drift 20.0m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Fixed_Mask_Ap_M1_L,
            ))
            pp.append(v.op_Fixed_Mask_Ap_M1_pp)
        elif el_name == 'Ap_M1':
            # Ap_M1: aperture 27.75m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Ap_M1_shape,
                _ap_or_ob='a',
                _Dx=v.op_Ap_M1_Dx,
                _Dy=v.op_Ap_M1_Dy,
                _x=v.op_Ap_M1_x,
                _y=v.op_Ap_M1_y,
            ))
            pp.append(v.op_Ap_M1_pp)
        elif el_name == 'M1':
            # M1: toroidalMirror 27.75m
            el.append(srwlib.SRWLOptMirTor(
                _rt=v.op_M1_rt,
                _rs=v.op_M1_rs,
                _size_tang=v.op_M1_size_tang,
                _size_sag=v.op_M1_size_sag,
                _x=v.op_M1_horizontalPosition,
                _y=v.op_M1_verticalPosition,
                _ap_shape=v.op_M1_ap_shape,
                _nvx=v.op_M1_nvx,
                _nvy=v.op_M1_nvy,
                _nvz=v.op_M1_nvz,
                _tvx=v.op_M1_tvx,
                _tvy=v.op_M1_tvy,
            ))
            pp.append(v.op_M1_pp)
            
        elif el_name == 'M1_M2':
            # M1_M2: drift 27.75m
            el.append(srwlib.SRWLOptD(
                _L=v.op_M1_M2_L,
            ))
            pp.append(v.op_M1_M2_pp)
##        elif el_name == 'M2':
##            # M2: mirror 33.75m
##            mirror_file = v.op_M2_hfn
##            assert os.path.isfile(mirror_file), \
##                'Missing input file {}, required by M2 beamline element'.format(mirror_file)
##            el.append(srwlib.srwl_opt_setup_surf_height_2d(
##                srwlib.srwl_uti_read_data_cols(mirror_file, "\t"),
##                _dim=v.op_M2_dim,
##                _ang=abs(v.op_M2_ang),
##                _amp_coef=v.op_M2_amp_coef,
##                _size_x=v.op_M2_size_x,
##                _size_y=v.op_M2_size_y,
##            ))
##            pp.append(v.op_M2_pp)
        elif el_name == 'M2_Before_Grating':
            # M2_Before_Grating: drift 33.75m
            el.append(srwlib.SRWLOptD(
                _L=v.op_M2_Before_Grating_L,
            ))
            pp.append(v.op_M2_Before_Grating_pp)
        elif el_name == 'Before_Grating':
            # Before_Grating: watch 34.25m
            pass
        elif el_name == 'Grating':
            # Grating: grating 34.25m
            mirror = srwlib.SRWLOptMirPl(
                _size_tang=v.op_Grating_size_tang,
                _size_sag=v.op_Grating_size_sag,
                _nvx=v.op_Grating_nvx,
                _nvy=v.op_Grating_nvy,
                _nvz=v.op_Grating_nvz,
                _tvx=v.op_Grating_tvx,
                _tvy=v.op_Grating_tvy,
                _x=v.op_Grating_x,
                _y=v.op_Grating_y,
            )
            el.append(srwlib.SRWLOptG(
                _mirSub=mirror,
                _m=v.op_Grating_m,
                _grDen=v.op_Grating_grDen,
                _grDen1=v.op_Grating_grDen1,
                _grDen2=v.op_Grating_grDen2,
                _grDen3=v.op_Grating_grDen3,
                _grDen4=v.op_Grating_grDen4,
            ))
            pp.append(v.op_Grating_pp)
        elif el_name == 'Gr_Surf_Height_Err_Before_M3':
            # Gr_Surf_Height_Err_Before_M3: drift 34.25m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Gr_Surf_Height_Err_Before_M3_L,
            ))
            pp.append(v.op_Gr_Surf_Height_Err_Before_M3_pp)
        elif el_name == 'Before_M3':
            # Before_M3: watch 36.75m
            pass
        elif el_name == 'M3':
            # M3: toroidalMirror 36.75m
            el.append(srwlib.SRWLOptMirTor(
                _rt=v.op_M3_rt,
                _rs=v.op_M3_rs,
                _size_tang=v.op_M3_size_tang,
                _size_sag=v.op_M3_size_sag,
                _x=v.op_M3_horizontalPosition,
                _y=v.op_M3_verticalPosition,
                _ap_shape=v.op_M3_ap_shape,
                _nvx=v.op_M3_nvx,
                _nvy=v.op_M3_nvy,
                _nvz=v.op_M3_nvz,
                _tvx=v.op_M3_tvx,
                _tvy=v.op_M3_tvy,
            ))
            pp.append(v.op_M3_pp)
            
        elif el_name == 'Lens_Before_Exit_Slit':
            # Lens_Before_Exit_Slit: drift 36.75m
            el.append(srwlib.SRWLOptD(
                _L=v.op_Lens_Before_Exit_Slit_L,
            ))
            pp.append(v.op_Lens_Before_Exit_Slit_pp)
        elif el_name == 'Before_Exit_Slit':
            # Before_Exit_Slit: watch 51.75m
            pass
        elif el_name == 'Exit_Slit':
            # Exit_Slit: aperture 51.75m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Exit_Slit_shape,
                _ap_or_ob='a',
                _Dx=v.op_Exit_Slit_Dx,
                _Dy=v.op_Exit_Slit_Dy,
                _x=v.op_Exit_Slit_x,
                _y=v.op_Exit_Slit_y,
            ))
            pp.append(v.op_Exit_Slit_pp)
        elif el_name == 'After_Exit_Slit':
            # After_Exit_Slit: watch 51.75m
            pass
        elif el_name == 'After_Exit_Slit_Before_ZP':
            # After_Exit_Slit_Before_ZP: drift 51.75m
            el.append(srwlib.SRWLOptD(
                _L=v.op_After_Exit_Slit_Before_ZP_L,
            ))
            pp.append(v.op_After_Exit_Slit_Before_ZP_pp)
        elif el_name == 'Before_ZP':
            # Before_ZP: watch 56.75m
            pass
        elif el_name == 'Ap_ZP':
            # Ap_ZP: aperture 56.75m
            el.append(srwlib.SRWLOptA(
                _shape=v.op_Ap_ZP_shape,
                _ap_or_ob='a',
                _Dx=v.op_Ap_ZP_Dx,
                _Dy=v.op_Ap_ZP_Dy,
                _x=v.op_Ap_ZP_x,
                _y=v.op_Ap_ZP_y,
            ))
            pp.append(v.op_Ap_ZP_pp)
        elif el_name == 'Zone_Plate':
            # Zone_Plate: zonePlate 56.75m
            el.append(srwlib.SRWLOptZP(
                _nZones=v.op_Zone_Plate_nZones,
                _rn=v.op_Zone_Plate_rn,
                _thick=v.op_Zone_Plate_thick,
                _delta1=v.op_Zone_Plate_delta1,
                _atLen1=v.op_Zone_Plate_atLen1,
                _delta2=v.op_Zone_Plate_delta2,
                _atLen2=v.op_Zone_Plate_atLen2,
                _x=v.op_Zone_Plate_x,
                _y=v.op_Zone_Plate_y,
            ))
            pp.append(v.op_Zone_Plate_pp)
        elif el_name == 'After_ZP':
            # After_ZP: watch 56.75m
            pass
        elif el_name == 'After_ZP_Watchpoint':
            # After_ZP_Watchpoint: drift 56.75m
            el.append(srwlib.SRWLOptD(
                _L=v.op_After_ZP_Watchpoint_L,
            ))
            pp.append(v.op_After_ZP_Watchpoint_pp)
        elif el_name == 'Watchpoint':
            # Watchpoint: watch 56.753227m
            pass
    pp.append(v.op_fin_pp)

    #print(pp)
    
    return srwlib.SRWLOptC(el, pp)


varParam = srwl_bl.srwl_uti_ext_options([
    ['name', 's', 'SXN_V02_250eV_realZP debug', 'simulation name'],

#---Data Folder
    ['fdir', 's', '', 'folder (directory) name for reading-in input and saving output data files'],

#---Electron Beam
    ['ebm_nm', 's', '', 'standard electron beam name'],
    ['ebm_nms', 's', '', 'standard electron beam name suffix: e.g. can be Day1, Final'],
    ['ebm_i', 'f', 0.5, 'electron beam current [A]'],
    ['ebm_e', 'f', 3.0, 'electron beam avarage energy [GeV]'],
    ['ebm_de', 'f', 0.0, 'electron beam average energy deviation [GeV]'],
    ['ebm_x', 'f', 0.0, 'electron beam initial average horizontal position [m]'],
    ['ebm_y', 'f', 0.0, 'electron beam initial average vertical position [m]'],
    ['ebm_xp', 'f', 0.0, 'electron beam initial average horizontal angle [rad]'],
    ['ebm_yp', 'f', 0.0, 'electron beam initial average vertical angle [rad]'],
    ['ebm_z', 'f', 0., 'electron beam initial average longitudinal position [m]'],
    ['ebm_dr', 'f', 0.0, 'electron beam longitudinal drift [m] to be performed before a required calculation'],
    ['ebm_ens', 'f', 0.00089, 'electron beam relative energy spread'],
    ['ebm_emx', 'f', 7.6e-10, 'electron beam horizontal emittance [m]'],
    ['ebm_emy', 'f', 8e-12, 'electron beam vertical emittance [m]'],
    # Definition of the beam through Moments:
    ['ebm_sigx', 'f', 3.73951868561e-05, 'horizontal RMS size of electron beam [m]'],
    ['ebm_sigy', 'f', 3.05941170816e-06, 'vertical RMS size of electron beam [m]'],
    ['ebm_sigxp', 'f', 2.03234711174e-05, 'horizontal RMS angular divergence of electron beam [rad]'],
    ['ebm_sigyp', 'f', 2.61488180184e-06, 'vertical RMS angular divergence of electron beam [rad]'],
    ['ebm_mxxp', 'f', 0.0, 'horizontal position-angle mixed 2nd order moment of electron beam [m]'],
    ['ebm_myyp', 'f', 0.0, 'vertical position-angle mixed 2nd order moment of electron beam [m]'],

#---Undulator
    ['und_bx', 'f', 0.0, 'undulator horizontal peak magnetic field [T]'],
    ['und_by', 'f', 0.72799921, 'undulator vertical peak magnetic field [T]'],
    ['und_phx', 'f', 0.0, 'initial phase of the horizontal magnetic field [rad]'],
    ['und_phy', 'f', 0.0, 'initial phase of the vertical magnetic field [rad]'],
    ['und_b2e', '', '', 'estimate undulator fundamental photon energy (in [eV]) for the amplitude of sinusoidal magnetic field defined by und_b or und_bx, und_by', 'store_true'],
    ['und_e2b', '', '', 'estimate undulator field amplitude (in [T]) for the photon energy defined by w_e', 'store_true'],
    ['und_per', 'f', 0.05, 'undulator period [m]'],
    ['und_len', 'f', 2.0, 'undulator length [m]'],
    ['und_zc', 'f', 1.25, 'undulator center longitudinal position [m]'],
    ['und_sx', 'i', -1, 'undulator horizontal magnetic field symmetry vs longitudinal position'],
    ['und_sy', 'i', 1, 'undulator vertical magnetic field symmetry vs longitudinal position'],
    ['und_g', 'f', 6.72, 'undulator gap [mm] (assumes availability of magnetic measurement or simulation data)'],
    ['und_ph', 'f', 0.0, 'shift of magnet arrays [mm] for which the field should be set up'],
    ['und_mdir', 's', '', 'name of magnetic measurements sub-folder'],
    ['und_mfs', 's', '', 'name of magnetic measurements for different gaps summary file'],



#---Calculation Types
    # Electron Trajectory
    ['tr', '', '', 'calculate electron trajectory', 'store_true'],
    ['tr_cti', 'f', 0.0, 'initial time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_ctf', 'f', 0.0, 'final time moment (c*t) for electron trajectory calculation [m]'],
    ['tr_np', 'f', 10000, 'number of points for trajectory calculation'],
    ['tr_mag', 'i', 1, 'magnetic field to be used for trajectory calculation: 1- approximate, 2- accurate'],
    ['tr_fn', 's', 'res_trj.dat', 'file name for saving calculated trajectory data'],
    ['tr_pl', 's', '', 'plot the resulting trajectiry in graph(s): ""- dont plot, otherwise the string should list the trajectory components to plot'],

    #Single-Electron Spectrum vs Photon Energy
    ['ss', '', '', 'calculate single-e spectrum vs photon energy', 'store_true'],
    ['ss_ei', 'f', 10.0, 'initial photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ef', 'f', 2100.0, 'final photon energy [eV] for single-e spectrum vs photon energy calculation'],
    ['ss_ne', 'i', 2000, 'number of points vs photon energy for single-e spectrum vs photon energy calculation'],
    ['ss_x', 'f', 0.0, 'horizontal position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_y', 'f', 0.0, 'vertical position [m] for single-e spectrum vs photon energy calculation'],
    ['ss_meth', 'i', 1, 'method to use for single-e spectrum vs photon energy calculation: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler"'],
    ['ss_prec', 'f', 0.01, 'relative precision for single-e spectrum vs photon energy calculation (nominal value is 0.01)'],
    ['ss_pol', 'i', 6, 'polarization component to extract after spectrum vs photon energy calculation: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['ss_mag', 'i', 1, 'magnetic field to be used for single-e spectrum vs photon energy calculation: 1- approximate, 2- accurate'],
    ['ss_ft', 's', 'f', 'presentation/domain: "f"- frequency (photon energy), "t"- time'],
    ['ss_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['ss_fn', 's', 'res_spec_se.dat', 'file name for saving calculated single-e spectrum vs photon energy'],
    ['ss_pl', 's', '', 'plot the resulting single-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],

    #Multi-Electron Spectrum vs Photon Energy (taking into account e-beam emittance, energy spread and collection aperture size)
    ['sm', '', '', 'calculate multi-e spectrum vs photon energy', 'store_true'],
    ['sm_ei', 'f', 10.0, 'initial photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ef', 'f', 2000.0, 'final photon energy [eV] for multi-e spectrum vs photon energy calculation'],
    ['sm_ne', 'i', 5000, 'number of points vs photon energy for multi-e spectrum vs photon energy calculation'],
    ['sm_x', 'f', 0.0, 'horizontal center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_rx', 'f', 0.004, 'range of horizontal position / horizontal aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_nx', 'i', 1, 'number of points vs horizontal position for multi-e spectrum vs photon energy calculation'],
    ['sm_y', 'f', 0.0, 'vertical center position [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ry', 'f', 0.004, 'range of vertical position / vertical aperture size [m] for multi-e spectrum vs photon energy calculation'],
    ['sm_ny', 'i', 1, 'number of points vs vertical position for multi-e spectrum vs photon energy calculation'],
    ['sm_mag', 'i', 1, 'magnetic field to be used for calculation of multi-e spectrum spectrum or intensity distribution: 1- approximate, 2- accurate'],
    ['sm_hi', 'i', 1, 'initial UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_hf', 'i', 15, 'final UR spectral harmonic to be taken into account for multi-e spectrum vs photon energy calculation'],
    ['sm_prl', 'f', 1.0, 'longitudinal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_pra', 'f', 1.0, 'azimuthal integration precision parameter for multi-e spectrum vs photon energy calculation'],
    ['sm_meth', 'i', -1, 'method to use for spectrum vs photon energy calculation in case of arbitrary input magnetic field: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler", -1- dont use this accurate integration method (rather use approximate if possible)'],
    ['sm_prec', 'f', 0.01, 'relative precision for spectrum vs photon energy calculation in case of arbitrary input magnetic field (nominal value is 0.01)'],
    ['sm_nm', 'i', 1, 'number of macro-electrons for calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_na', 'i', 5, 'number of macro-electrons to average on each node at parallel (MPI-based) calculation of spectrum in case of arbitrary input magnetic field'],
    ['sm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons) for intermediate intensity at calculation of multi-electron spectrum in case of arbitrary input magnetic field'],
    ['sm_type', 'i', 1, 'calculate flux (=1) or flux per unit surface (=2)'],
    ['sm_pol', 'i', 6, 'polarization component to extract after calculation of multi-e flux or intensity: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['sm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['sm_fn', 's', 'res_spec_me.dat', 'file name for saving calculated milti-e spectrum vs photon energy'],
    ['sm_pl', 's', '', 'plot the resulting spectrum-e spectrum in a graph: ""- dont plot, "e"- show plot vs photon energy'],
    #to add options for the multi-e calculation from "accurate" magnetic field

    #Power Density Distribution vs horizontal and vertical position
    ['pw', '', '', 'calculate SR power density distribution', 'store_true'],
    ['pw_x', 'f', 0.0, 'central horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_rx', 'f', 0.05, 'range of horizontal position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_nx', 'i', 100, 'number of points vs horizontal position for calculation of power density distribution'],
    ['pw_y', 'f', 0.0, 'central vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ry', 'f', 0.05, 'range of vertical position [m] for calculation of power density distribution vs horizontal and vertical position'],
    ['pw_ny', 'i', 100, 'number of points vs vertical position for calculation of power density distribution'],
    ['pw_pr', 'f', 1.0, 'precision factor for calculation of power density distribution'],
    ['pw_meth', 'i', 1, 'power density computation method (1- "near field", 2- "far field")'],
    ['pw_zst', 'f', 0., 'initial longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_zfi', 'f', 0., 'final longitudinal position along electron trajectory of power density distribution (effective if pow_sst < pow_sfi)'],
    ['pw_mag', 'i', 1, 'magnetic field to be used for power density calculation: 1- approximate, 2- accurate'],
    ['pw_fn', 's', 'res_pow.dat', 'file name for saving calculated power density distribution'],
    ['pw_pl', 's', '', 'plot the resulting power density distribution in a graph: ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    #Single-Electron Intensity distribution vs horizontal and vertical position
    ['si', '', '', 'calculate single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position', 'store_true'],
    #Single-Electron Wavefront Propagation
    ['ws', '', '', 'calculate single-electron (/ fully coherent) wavefront propagation', 'store_true'],
    #Multi-Electron (partially-coherent) Wavefront Propagation
    ['wm', '', '', 'calculate multi-electron (/ partially coherent) wavefront propagation', 'store_true'],

    ['w_e', 'f', 250.0, 'photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ef', 'f', -1.0, 'final photon energy [eV] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ne', 'i', 1, 'number of points vs photon energy for calculation of intensity distribution'],
    ['w_x', 'f', 0.0, 'central horizontal position [m] for calculation of intensity distribution'],
    ['w_rx', 'f', 0.004, 'range of horizontal position [m] for calculation of intensity distribution'],
    ['w_nx', 'i', 100, 'number of points vs horizontal position for calculation of intensity distribution'],
    ['w_y', 'f', 0.0, 'central vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ry', 'f', 0.004, 'range of vertical position [m] for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_ny', 'i', 100, 'number of points vs vertical position for calculation of intensity distribution'],
    ['w_smpf', 'f', 0.3, 'sampling factor for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_meth', 'i', 1, 'method to use for calculation of intensity distribution vs horizontal and vertical position: 0- "manual", 1- "auto-undulator", 2- "auto-wiggler"'],
    ['w_prec', 'f', 0.01, 'relative precision for calculation of intensity distribution vs horizontal and vertical position'],
    ['w_u', 'i', 1, 'electric field units: 0- arbitrary, 1- sqrt(Phot/s/0.1%bw/mm^2), 2- sqrt(J/eV/mm^2) or sqrt(W/mm^2), depending on representation (freq. or time)'],
    ['si_pol', 'i', 6, 'polarization component to extract after calculation of intensity distribution: 0- Linear Horizontal, 1- Linear Vertical, 2- Linear 45 degrees, 3- Linear 135 degrees, 4- Circular Right, 5- Circular Left, 6- Total'],
    ['si_type', 'i', 0, 'type of a characteristic to be extracted after calculation of intensity distribution: 0- Single-Electron Intensity, 1- Multi-Electron Intensity, 2- Single-Electron Flux, 3- Multi-Electron Flux, 4- Single-Electron Radiation Phase, 5- Re(E): Real part of Single-Electron Electric Field, 6- Im(E): Imaginary part of Single-Electron Electric Field, 7- Single-Electron Intensity, integrated over Time or Photon Energy'],
    ['w_mag', 'i', 1, 'magnetic field to be used for calculation of intensity distribution vs horizontal and vertical position: 1- approximate, 2- accurate'],

    ['si_fn', 's', 'res_int_se.dat', 'file name for saving calculated single-e intensity distribution (without wavefront propagation through a beamline) vs horizontal and vertical position'],
    ['si_pl', 's', '', 'plot the input intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],
    ['ws_fni', 's', 'res_int_pr_se.dat', 'file name for saving propagated single-e intensity distribution vs horizontal and vertical position'],
    ['ws_pl', 's', '', 'plot the resulting intensity distributions in graph(s): ""- dont plot, "x"- vs horizontal position, "y"- vs vertical position, "xy"- vs horizontal and vertical position'],

    ['wm_nm', 'i', 15000, 'number of macro-electrons (coherent wavefronts) for calculation of multi-electron wavefront propagation'],
    ['wm_na', 'i', 5, 'number of macro-electrons (coherent wavefronts) to average on each node for parallel (MPI-based) calculation of multi-electron wavefront propagation'],
    ['wm_ns', 'i', 5, 'saving periodicity (in terms of macro-electrons / coherent wavefronts) for intermediate intensity at multi-electron wavefront propagation calculation'],
    ['wm_ch', 'i', 40, 'type of a characteristic to be extracted after calculation of multi-electron wavefront propagation: #0- intensity (s0); 1- four Stokes components; 2- mutual intensity cut vs x; 3- mutual intensity cut vs y; 40- intensity(s0), mutual intensity cuts and degree of coherence vs X & Y'],
    ['wm_ap', 'i', 0, 'switch specifying representation of the resulting Stokes parameters: coordinate (0) or angular (1)'],
    ['wm_x0', 'f', 0, 'horizontal center position for mutual intensity cut calculation'],
    ['wm_y0', 'f', 0, 'vertical center position for mutual intensity cut calculation'],
    ['wm_ei', 'i', 0, 'integration over photon energy is required (1) or not (0); if the integration is required, the limits are taken from w_e, w_ef'],
    ['wm_rm', 'i', 1, 'method for generation of pseudo-random numbers for e-beam phase-space integration: 1- standard pseudo-random number generator, 2- Halton sequences, 3- LPtau sequences (to be implemented)'],
    ['wm_am', 'i', 0, 'multi-electron integration approximation method: 0- no approximation (use the standard 5D integration method), 1- integrate numerically only over e-beam energy spread and use convolution to treat transverse emittance'],
    ['wm_fni', 's', 'res_int_pr_me.dat', 'file name for saving propagated multi-e intensity distribution vs horizontal and vertical position'],

    #to add options
    ['op_r', 'f', 20.0, 'longitudinal position of the first optical element [m]'],

    # Former appParam:
    ['rs_type', 's', 'u', 'source type, (u) idealized undulator, (t), tabulated undulator, (m) multipole, (g) gaussian beam'],

#---Beamline optics:
    # Fixed_Mask: aperture
    ['op_Fixed_Mask_shape', 's', 'r', 'shape'],
    ['op_Fixed_Mask_Dx', 'f', 0.004, 'horizontalSize'],
    ['op_Fixed_Mask_Dy', 'f', 0.004, 'verticalSize'],
    ['op_Fixed_Mask_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Fixed_Mask_y', 'f', 0.0, 'verticalOffset'],

    # Fixed_Mask_Ap_M1: drift
    ['op_Fixed_Mask_Ap_M1_L', 'f', 7.75, 'length'],

    # Ap_M1: aperture
    ['op_Ap_M1_shape', 's', 'r', 'shape'],
    ['op_Ap_M1_Dx', 'f', 0.005, 'horizontalSize'],
    ['op_Ap_M1_Dy', 'f', 0.005, 'verticalSize'],
    ['op_Ap_M1_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Ap_M1_y', 'f', 0.0, 'verticalOffset'],

    # M1: toroidalMirror
    ['op_M1_hfn', 's', 'None', 'heightProfileFile'],
    ['op_M1_dim', 's', 'x', 'orientation'],
    ['op_M1_ap_shape', 's', 'r', 'apertureShape'],
    ['op_M1_rt', 'f', 1e+23, 'tangentialRadius'],
    ['op_M1_rs', 'f', 1.04058, 'sagittalRadius'],
    ['op_M1_size_tang', 'f', 0.3, 'tangentialSize'],
    ['op_M1_size_sag', 'f', 0.015, 'sagittalSize'],
    ['op_M1_ang', 'f', 0.019635, 'grazingAngle'],
    ['op_M1_horizontalPosition', 'f', 0.0, 'horizontalPosition'],
    ['op_M1_verticalPosition', 'f', 0.0, 'verticalPosition'],
    ['op_M1_nvx', 'f', 0.999807239581, 'normalVectorX'],
    ['op_M1_nvy', 'f', 0.0, 'normalVectorY'],
    ['op_M1_nvz', 'f', -0.0196337383668, 'normalVectorZ'],
    ['op_M1_tvx', 'f', 0.0196337383668, 'tangentialVectorX'],
    ['op_M1_tvy', 'f', 0.0, 'tangentialVectorY'],
    ['op_M1_amp_coef', 'f', 0.0001, 'heightAmplification'],

    # M1_M2: drift
    ['op_M1_M2_L', 'f', 6.0, 'length'],

    # M2: mirror
    ['op_M2_hfn', 's', 'M2err.dat', 'heightProfileFile'],
    ['op_M2_dim', 's', 'y', 'orientation'],
    ['op_M2_ang', 'f', 0.043119085, 'grazingAngle'],
    ['op_M2_amp_coef', 'f', 0.0001, 'heightAmplification'],
    ['op_M2_size_x', 'f', 0.02, 'horizontalTransverseSize'],
    ['op_M2_size_y', 'f', 0.014, 'verticalTransverseSize'],

    # M2_Before_Grating: drift
    ['op_M2_Before_Grating_L', 'f', 0.5, 'length'],

    # Grating: grating
    ['op_Grating_size_tang', 'f', 0.2, 'tangentialSize'],
    ['op_Grating_size_sag', 'f', 0.02, 'sagittalSize'],
    ['op_Grating_nvx', 'f', 0.0, 'normalVectorX'],
    ['op_Grating_nvy', 'f', -0.999405274299, 'normalVectorY'],
    ['op_Grating_nvz', 'f', -0.0344832960142, 'normalVectorZ'],
    ['op_Grating_tvx', 'f', 0.0, 'tangentialVectorX'],
    ['op_Grating_tvy', 'f', -0.0344832960142, 'tangentialVectorY'],
    ['op_Grating_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Grating_y', 'f', 0.0, 'verticalOffset'],
    ['op_Grating_m', 'f', 1.0, 'diffractionOrder'],
    ['op_Grating_grDen', 'f', 150.0, 'grooveDensity0'],
    ['op_Grating_grDen1', 'f', 0.0, 'grooveDensity1'],
    ['op_Grating_grDen2', 'f', 0.0, 'grooveDensity2'],
    ['op_Grating_grDen3', 'f', 0.0, 'grooveDensity3'],
    ['op_Grating_grDen4', 'f', 0.0, 'grooveDensity4'],

    # Gr_Surf_Height_Err_Before_M3: drift
    ['op_Gr_Surf_Height_Err_Before_M3_L', 'f', 2.5, 'length'],

    # M3: toroidalMirror
    ['op_M3_hfn', 's', 'None', 'heightProfileFile'],
    ['op_M3_dim', 's', 'x', 'orientation'],
    ['op_M3_ap_shape', 's', 'r', 'apertureShape'],
    ['op_M3_rt', 'f', 1074.128, 'tangentialRadius'],
    ['op_M3_rs', 'f', 0.58901, 'sagittalRadius'],
    ['op_M3_size_tang', 'f', 0.38, 'tangentialSize'],
    ['op_M3_size_sag', 'f', 0.03, 'sagittalSize'],
    ['op_M3_ang', 'f', 0.019635, 'grazingAngle'],
    ['op_M3_horizontalPosition', 'f', 0.0, 'horizontalPosition'],
    ['op_M3_verticalPosition', 'f', 0.0, 'verticalPosition'],
    ['op_M3_nvx', 'f', 0.999807239581, 'normalVectorX'],
    ['op_M3_nvy', 'f', 0.0, 'normalVectorY'],
    ['op_M3_nvz', 'f', -0.0196337383668, 'normalVectorZ'],
    ['op_M3_tvx', 'f', 0.0196337383668, 'tangentialVectorX'],
    ['op_M3_tvy', 'f', 0.0, 'tangentialVectorY'],
    ['op_M3_amp_coef', 'f', 0.0001, 'heightAmplification'],

    # Lens_Before_Exit_Slit: drift
    ['op_Lens_Before_Exit_Slit_L', 'f', 15.0, 'length'],

    # Exit_Slit: aperture
    ['op_Exit_Slit_shape', 's', 'r', 'shape'],
    ['op_Exit_Slit_Dx', 'f', 2e-05, 'horizontalSize'],
    ['op_Exit_Slit_Dy', 'f', 2e-05, 'verticalSize'],
    ['op_Exit_Slit_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Exit_Slit_y', 'f', 0.0, 'verticalOffset'],

    # After_Exit_Slit_Before_ZP: drift
    ['op_After_Exit_Slit_Before_ZP_L', 'f', 5.0, 'length'],

    # Ap_ZP: aperture
    ['op_Ap_ZP_shape', 's', 'c', 'shape'],
    ['op_Ap_ZP_Dx', 'f', 0.00032, 'horizontalSize'],
    ['op_Ap_ZP_Dy', 'f', 0.00032, 'verticalSize'],
    ['op_Ap_ZP_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Ap_ZP_y', 'f', 0.0, 'verticalOffset'],

    # Zone_Plate: zonePlate
    ['op_Zone_Plate_rn', 'f', 0.00016, 'outerRadius'],
    ['op_Zone_Plate_thick', 'f', 0.0001, 'thickness'],
    ['op_Zone_Plate_delta1', 'f', 0.007639, 'mainRefractiveIndex'],
    ['op_Zone_Plate_atLen1', 'f', 3.680028e-08, 'mainAttenuationLength'],
    ['op_Zone_Plate_delta2', 'f', 0.0, 'complementaryRefractiveIndex'],
    ['op_Zone_Plate_atLen2', 'f', 1000000.0, 'complementaryAttenuationLength'],
    ['op_Zone_Plate_x', 'f', 0.0, 'horizontalOffset'],
    ['op_Zone_Plate_y', 'f', 0.0, 'verticalOffset'],
    ['op_Zone_Plate_nZones', 'i', 1600, 'numberOfZones'],

    # After_ZP_Watchpoint: drift
    ['op_After_ZP_Watchpoint_L', 'f', 0.003227, 'length'],

#---Propagation parameters
    ['op_Fixed_Mask_pp', 'f',                   [0, 0, 1.0, 0, 0, 1.2, 12.0, 1.6, 12.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Fixed_Mask'],
    ['op_Fixed_Mask_Ap_M1_pp', 'f',             [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Fixed_Mask_Ap_M1'],
    ['op_Ap_M1_pp', 'f',                        [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Ap_M1'],
    ['op_M1_pp', 'f',                           [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M1'],
    ['op_M1_M2_pp', 'f',                        [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M1_M2'],
    ['op_M2_pp', 'f',                           [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M2'],
    ['op_M2_Before_Grating_pp', 'f',            [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M2_Before_Grating'],
    ['op_Grating_pp', 'f',                      [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, -0.0861313174, 0.99628379, 1.0, 0.0], 'Grating'],
    ['op_Gr_Surf_Height_Err_Before_M3_pp', 'f', [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Gr_Surf_Height_Err_Before_M3'],
    ['op_M3_pp', 'f',                           [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'M3'],
    ['op_Lens_Before_Exit_Slit_pp', 'f',        [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Lens_Before_Exit_Slit'],

    ['op_Exit_Slit_pp', 'f',                    [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Exit_Slit'],
    ['op_After_Exit_Slit_Before_ZP_pp', 'f',    [0, 0, 1.0, 3, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'After_Exit_Slit_Before_ZP'],
    ['op_Ap_ZP_pp', 'f',                        [0, 0, 1.0, 1, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Ap_ZP'],

    ['op_Zone_Plate_pp', 'f',                   [0, 0, 1.0, 0, 0, 0.03, 800.0, 0.03, 800.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'Zone_Plate'],
    
    ['op_After_ZP_Watchpoint_pp', 'f',          [0, 0, 1.0, 0, 0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'After_ZP_Watchpoint'],

    ['op_fin_pp', 'f',                          [0, 0, 1.0, 0, 0, 0.01, 2.0, 0.01, 2.0, 3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'final post-propagation (resize) parameters'],

    #[ 0]: Auto-Resize (1) or not (0) Before propagation
    #[ 1]: Auto-Resize (1) or not (0) After propagation
    #[ 2]: Relative Precision for propagation with Auto-Resizing (1. is nominal)
    #[ 3]: Allow (1) or not (0) for semi-analytical treatment of the quadratic (leading) phase terms at the propagation
    #[ 4]: Do any Resizing on Fourier side, using FFT, (1) or not (0)
    #[ 5]: Horizontal Range modification factor at Resizing (1. means no modification)
    #[ 6]: Horizontal Resolution modification factor at Resizing
    #[ 7]: Vertical Range modification factor at Resizing
    #[ 8]: Vertical Resolution modification factor at Resizing
    #[ 9]: Type of wavefront Shift before Resizing: 1- vs Hor. Position, 2- vs Vert. Position, 3- vs Hor. and Vert. Position
    #[10]: New Horizontal wavefront Center position after Shift
    #[11]: New Vertical wavefront Center position after Shift
    #[12]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Horizontal Coordinate
    #[13]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Vertical Coordinate
    #[14]: Optional: Orientation of the Output Optical Axis vector in the Incident Beam Frame: Longitudinal Coordinate
    #[15]: Optional: Orientation of the Horizontal Base vector of the Output Frame in the Incident Beam Frame: Horizontal Coordinate
    #[16]: Optional: Orientation of the Horizontal Base vector of the Output Frame in the Incident Beam Frame: Vertical Coordinate
])


def main():
    v = srwl_bl.srwl_uti_parse_options(varParam, use_sys_argv=True)
    op = set_optics(v)
    v.ws = True
    v.ws_pl = 'xy'
    mag = None
    if v.rs_type == 'm':
        mag = srwlib.SRWLMagFldC()
        mag.arXc.append(0)
        mag.arYc.append(0)
        mag.arMagFld.append(srwlib.SRWLMagFldM(v.mp_field, v.mp_order, v.mp_distribution, v.mp_len))
        mag.arZc.append(v.mp_zc)
    srwl_bl.SRWLBeamline(_name=v.name, _mag_approx=mag).calc_all(v, op)


if __name__ == '__main__':
    main()
