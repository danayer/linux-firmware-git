%global debug_package %{nil}
	
 
	
%global _firmwarepath	/usr/lib/firmware
	
%define _binaries_in_noarch_packages_terminate_build 0

%global commit a60087f7c9254065efb9e641b66af67e4c57b29f

%global shortcommit a60087f
 
	
Name:		linux-firmware
	
Version:    20250321.1.1
	
Release:	1%{?dist}
	
Summary:	Firmware files used by the Linux kernel
	
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
	
URL:		http://www.kernel.org/
	
BuildArch:	noarch
	
 
	
Source0:	https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/snapshot/linux-firmware-main.tar.gz
	
 
	
BuildRequires:	make
	
BuildRequires:	git-core
	
BuildRequires:	python3
	
%if %{undefined rhel}
	
# Not required but de-dupes FW so reduces size
	
BuildRequires:	rdfind
	
%endif
	
 
	
Requires:	linux-firmware-whence
	
Recommends:	amd-gpu-firmware
	
Recommends:	amd-ucode-firmware
	
Recommends:	atheros-firmware
	
Recommends:	brcmfmac-firmware
	
Recommends:	cirrus-audio-firmware
	
Recommends:	intel-audio-firmware
	
Recommends:	intel-gpu-firmware
	
Recommends:	mt7xxx-firmware
	
Recommends:	nvidia-gpu-firmware
	
Recommends:	nxpwireless-firmware
	
Recommends:	realtek-firmware
	
Recommends:	tiwilink-firmware
	
 
	
%description
	
This package includes firmware files required for some devices to
	
operate.
	
 
	
%package whence
	
Summary:	WHENCE License file
	
License:	GPL-1.0-or-later AND GPL-2.0-or-later AND MIT AND LicenseRef-Callaway-Redistributable-no-modification-permitted
	
%description whence
	
This package contains the WHENCE license file which documents the vendor license details.
	
 
	
# GPU firmwares
	
%package -n amd-gpu-firmware
	
Summary:	Firmware for AMD GPUs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n amd-gpu-firmware
	
Firmware for AMD amdgpu and radeon GPUs.
	
 
	
%package -n intel-gpu-firmware
	
Summary:	Firmware for Intel GPUs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n intel-gpu-firmware
	
Firmware for Intel GPUs including GuC (Graphics Microcontroller), HuC (HEVC/H.265
	
Microcontroller) and DMC (Display Microcontroller) firmware for Skylake and later
	
platforms.
	
 
	
%package -n nvidia-gpu-firmware
	
Summary:	Firmware for NVIDIA GPUs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n nvidia-gpu-firmware
	
Firmware for NVIDIA GPUs.
	
 
	
# Microcode updates
	
%package -n amd-ucode-firmware
	
Summary:	Microcode updates for AMD CPUs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n amd-ucode-firmware
	
Microcode updates for AMD CPUs, AMD SEV and AMD TEE.
	
 
	
# WiFi/Bluetooth firmwares
	
%package -n atheros-firmware
	
Summary:	Firmware for Qualcomm Atheros WiFi/Bluetooth adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n atheros-firmware
	
Firmware for Qualcomm Atheros ath6k/ath9k/ath10k/ath11k WiFi adapters.
	
 
	
%package -n brcmfmac-firmware
	
Summary:	Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n brcmfmac-firmware
	
Firmware for Broadcom/Cypress brcmfmac WiFi/Bluetooth adapters.
	
 
	
%package -n iwlegacy-firmware
	
Summary:	Firmware for Intel(R) Wireless WiFi Link 3945(A)BG and 4965AGN adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n iwlegacy-firmware
	
This package contains the firmware required by the iwlegacy driver
	
for Linux. This includes the 3945(A)BG and 4965AGN WiFi NICs. Usage
	
of the firmware is subject to the terms and conditions contained
	
inside the provided LICENSE file. Please read it carefully.
	
 
	
%package -n iwlwifi-dvm-firmware
	
Summary:	DVM Firmware for Intel(R) Wireless WiFi adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n iwlwifi-dvm-firmware
	
This package contains the firmware required by the iwlwifi driver
	
for Linux built with DVM firmware support (CONFIG_IWLDVM=y/m). Usage of
	
the firmware is subject to the terms and conditions contained inside the
	
provided LICENSE file. Please read it carefully.
	
 
	
%package -n iwlwifi-mvm-firmware
	
Summary:	MVM Firmware for Intel(R) Wireless WiFi adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n iwlwifi-mvm-firmware
	
This package contains the firmware required by the iwlwifi driver
	
for Linux built with MVM firmware support (CONFIG_IWLMVM=y/m).  Usage of
	
the firmware is subject to the terms and conditions contained inside the
	
provided LICENSE file. Please read it carefully.
	
 
	
%package -n libertas-firmware
	
Summary:	Firmware for Marvell Libertas SD/USB WiFi Network Adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n libertas-firmware
	
Firmware for the Marvell Libertas series of WiFi Network Adapters
	
Including the SD 8686/8787 and USB 8388/8388.
	
 
	
%package -n mt7xxx-firmware
	
Summary:	Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n mt7xxx-firmware
	
Firmware for Mediatek 7600/7900 series WiFi/Bluetooth adapters
	
 
	
%package -n nxpwireless-firmware
	
Summary:	Firmware for NXP WiFi/Bluetooth/UWB adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n nxpwireless-firmware
	
Firmware for NXP WiFi/Bluetooth/UWB adapters.
	
 
	
%package -n realtek-firmware
	
Summary:	Firmware for Realtek WiFi/Bluetooth adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n realtek-firmware
	
Firmware for Realtek WiFi/Bluetooth adapters
	
 
	
%package -n tiwilink-firmware
	
Summary:	Firmware for Texas Instruments WiFi/Bluetooth adapters
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n tiwilink-firmware
	
Firmware for Texas Instruments WiFi/Bluetooth adapters
	
 
	
# SMART NIC and network switch firmwares
	
%package -n liquidio-firmware
	
Summary:	Firmware for Cavium LiquidIO Intelligent Server Adapter
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n liquidio-firmware
	
Firmware for Cavium LiquidIO Intelligent Server Adapter
	
 
	
%package -n mlxsw_spectrum-firmware
	
Summary:	Firmware for Mellanox Spectrum 1/2/3 Switches
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n mlxsw_spectrum-firmware
	
Firmware for Mellanox Spectrumi series 1/2/3 ethernet switches.
	
 
	
%package -n mrvlprestera-firmware
	
Summary:	Firmware for Marvell Prestera Switchdev/ASIC devices
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n mrvlprestera-firmware
	
Firmware for Marvell Prestera Switchdev/ASIC devices
	
 
	
%package -n netronome-firmware
	
Summary:	Firmware for Netronome Smart NICs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n netronome-firmware
	
Firmware for Netronome Smart NICs
	
 
	
%package -n qed-firmware
	
Summary:	Firmware for Marvell FastLinQ adapters family
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n qed-firmware
	
Firmware for Marvell FastLinQ adapters family (QDE), this device
	
supports RoCE (RDMA over Converged Ethernet), iSCSI, iWARP, FCoE
	
and ethernet including SRIOV, DCB etc.
	
 
	
# Silicon Vendor specific
	
%package -n qcom-firmware
	
Summary:	Firmware for Qualcomm SoCs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
Requires:	atheros-firmware = %{version}-%{release}
	
%description -n qcom-firmware
	
Firmware for various compoents in Qualcomm SoCs including Adreno
	
GPUs, Venus video encode/decode, Audio DSP, Compute DSP, WWAN
	
modem, Sensor DSPs.
	
 
	
# Vision and ISP hardware
	
%package -n intel-vsc-firmware
	
Summary:	Firmware files for Intel Visual Sensing Controller (IVSC)
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n intel-vsc-firmware
	
Firmware files for Intel Visual Sensing Controller (IVSC) for
	
Tiger Lake, Alder Lake and Raptor Lake SoCs and the IPU3/6 firmware.
	
 
	
# Sound codec hardware
	
%package -n cirrus-audio-firmware
	
Summary:	Firmware for Cirrus audio amplifiers and codecs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n cirrus-audio-firmware
	
Firmware for Cirrus audio amplifiers and codecs
	
 
	
%package -n intel-audio-firmware
	
Summary:	Firmware for Intel audio DSP amplifiers and codecs
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n intel-audio-firmware
	
Firmware for Intel audio DSP amplifiers and codecs
	
 
	
# Random other hardware
	
%package -n dvb-firmware
	
Summary:	Firmware for various DVB broadcast receivers
	
License:	LicenseRef-Callaway-Redistributable-no-modification-permitted
	
Requires:	linux-firmware-whence
	
%description -n dvb-firmware
	
Firmware for various DVB broadcast receivers. These include the
	
Siano DTV devices, devices based on Conexant chipsets (cx18,
	
cx23885, cx23840, cx231xx), Xceive xc4000/xc5000, DiBcom dib0700,
	
Terratec H5 DRX-K, ITEtech IT9135 Ax and Bx, and av7110.
	
 
	
%prep
	
%autosetup -S git -p1 -n linux-firmware-main
	
 
	
%build
	
 
	
%install
	
mkdir -p %{buildroot}/%{_firmwarepath}
	
mkdir -p %{buildroot}/%{_firmwarepath}/updates
	
 
	
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} install-xz
	
%if %{undefined rhel}
	
make DESTDIR=%{buildroot}/ FIRMWAREDIR=%{_firmwarepath} dedup
	
%endif
	
 
	
#Cleanup files we don't want to ship
	
pushd %{buildroot}/%{_firmwarepath}
	
# Remove firmware shipped in separate packages already
	
# Perhaps these should be built as subpackages of linux-firmware?
	
rm -rf ess korg sb16 yamaha
	
 
	
# Remove firmware for Creative CA0132 HD as it's in alsa-firmware
	
rm -f ctefx.bin* ctspeq.bin*
	
 
	
# Remove source files we don't need to install
	
rm -rf carl9170fw
	
rm -rf cis/{src,Makefile}
	
rm -f atusb/ChangeLog
	
rm -f av7110/{Boot.S,Makefile}
	
rm -f dsp56k/{bootstrap.asm,concat-bootstrap.pl,Makefile}
	
rm -f iscis/{*.c,*.h,README,Makefile}
	
rm -f keyspan_pda/{keyspan_pda.S,xircom_pgs.S,Makefile}
	
rm -f usbdux/*dux */*.asm
	
 
	
# No need to install old firmware versions where we also provide newer versions
	
# which are preferred and support the same (or more) hardware
	
rm -f libertas/sd8686_v8*
	
rm -f libertas/usb8388_v5.bin*
	
 
	
# Remove superfluous infra files
	
rm -f check_whence.py Makefile README
	
popd
	
 
	
# Create file list but exclude firmwares that we place in subpackages
	
pushd %{buildroot}/%{_firmwarepath}
	
# Генерируем списки файлов 
	
find . \! -type d | sed -e 's:^./::' > %{_builddir}/linux-firmware-main/linux-firmware.files
	
find . -type d | sed -e '/^.$/d' -e 's:^./::' > %{_builddir}/linux-firmware-main/linux-firmware.dirs
	
popd
	
# Изменим эту часть:
	
cd %{_builddir}/linux-firmware-main
	
# Разделите фильтрацию на несколько команд
sed -i \
  -e '/^a300_p/d' \
  -e '/^amdgpu/d' \
  -e '/^amdnpu/d' \
  -e '/^amd/d' \
  -e '/^amdtee/d' \
  -e '/^amd-ucode/d' \
  -e '/^ar3k/d' \
  -e '/^ath6k/d' \
  -e '/^ath9k_htc/d' \
  -e '/^ath10k/d' \
  -e '/^ath11k/d' \
  -e '/^ath12k/d' \
  -e '/^as102_data/d' \
  -e '/^av7110/d' \
  -e '/^brcm/d' \
  -e '/^cirrus/d' \
  -e '/^cmmb/d' \
  -e '/^cypress/d' \
  -e '/^dvb/d' \
  -e '/^i915/d' \
  -e '/^intel\/avs/d' \
  -e '/^intel\/catpt/d' \
  -e '/^intel\/dsp_fw/d' \
  -e '/^intel\/fw_sst/d' \
  -e '/^intel\/ipu/d' \
  -e '/^intel\/ipu3/d' \
  -e '/^intel\/irci_irci/d' \
  -e '/^intel\/vsc/d' \
  -e '/^isdbt/d' \
  -e '/^iwlwifi/d' \
  -e '/^nvidia\/a/d' \
  -e '/^nvidia\/g/d' \
  -e '/^nvidia\/tu/d' \
  -e '/^lgs8g75/d' \
  -e '/^libertas/d' \
  -e '/^liquidio/d' \
  -e '/^mellanox/d' \
  -e '/^mediatek\/mt76/d' \
  -e '/^mediatek\/mt79/d' \
  -e '/^mediatek\/BT/d' \
  -e '/^mediatek\/WIFI/d' \
  -e '/^mrvl\/prestera/d' \
  -e '/^mrvl\/sd8787/d' \
  -e '/^mt76/d' \
  -e '/^netronome/d' \
  -e '/^nxp/d' \
  -e '/^qca/d' \
  -e '/^qcom/d' \
  -e '/^qed/d' \
  -e '/^radeon/d' \
  -e '/^rtl_bt/d' \
  -e '/^rtlwifi/d' \
  -e '/^rtw88/d' \
  -e '/^rtw89/d' \
  -e '/^sms1xxx/d' \
  -e '/^tdmb/d' \
  -e '/^ti-connectivity/d' \
  -e '/^v4l-cx2/d' \
  linux-firmware.files
	
# Добавляем пути и форматирование
sed -i -e 's!^!/usr/lib/firmware/!' linux-firmware.{files,dirs}
	
sed -i -e 's/^/"/;s/$/"/' linux-firmware.files
	
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files
	
 
	
 
	
%files -f linux-firmware.files
	
%dir %{_firmwarepath}
	
%license LICENCE.* LICENSE.* GPL*
	
 
	
%files whence
	
%license WHENCE
	
 
	
# GPU firmwares
	
%files -n amd-gpu-firmware
	
%license LICENSE.radeon LICENSE.amdgpu LICENSE.amdnpu
	
%{_firmwarepath}/amdgpu/
	
%{_firmwarepath}/amdnpu/
	
%{_firmwarepath}/radeon/
	
 
	
%files -n intel-gpu-firmware
	
%license LICENSE.i915
	
%{_firmwarepath}/i915/
	
 
	
%files -n nvidia-gpu-firmware
	
%license LICENCE.nvidia
	
%dir %{_firmwarepath}/nvidia/
	
%{_firmwarepath}/nvidia/a*/
	
%{_firmwarepath}/nvidia/g*/
	
%{_firmwarepath}/nvidia/tu*/
	
 
	
# Microcode updates
	
%files -n amd-ucode-firmware
	
%license LICENSE.amd-ucode
	
%{_firmwarepath}/amd/
	
%{_firmwarepath}/amdtee/
	
%{_firmwarepath}/amd-ucode/
	
 
	
# WiFi/Bluetooth firmwares
	
%files -n atheros-firmware
	
%license LICENCE.atheros_firmware
	
%license LICENSE.QualcommAtheros_ar3k
	
%license LICENSE.QualcommAtheros_ath10k
	
%license LICENCE.open-ath9k-htc-firmware
	
%license qca/NOTICE.txt
	
%{_firmwarepath}/ar3k/
	
%{_firmwarepath}/ath6k/
	
%{_firmwarepath}/ath9k_htc/
	
%{_firmwarepath}/ath10k/
	
%{_firmwarepath}/ath11k/
	
%{_firmwarepath}/ath12k/
	
%{_firmwarepath}/qca/
	
 
	
%files -n brcmfmac-firmware
	
%license LICENCE.broadcom_bcm43xx
	
%license LICENCE.cypress
	
%{_firmwarepath}/brcm/
	
%{_firmwarepath}/cypress/
	
 
	
%files -n iwlegacy-firmware
	
%license LICENCE.iwlwifi_firmware
	
%{_firmwarepath}/iwlwifi-3945-*.ucode*
	
%{_firmwarepath}/iwlwifi-4965-*.ucode*
	
 
	
%files -n iwlwifi-dvm-firmware
	
%license LICENCE.iwlwifi_firmware
	
%{_firmwarepath}/iwlwifi-100-*.ucode*
	
%{_firmwarepath}/iwlwifi-105-*.ucode*
	
%{_firmwarepath}/iwlwifi-135-*.ucode*
	
%{_firmwarepath}/iwlwifi-1000-*.ucode*
	
%{_firmwarepath}/iwlwifi-2000-*.ucode*
	
%{_firmwarepath}/iwlwifi-2030-*.ucode*
	
%{_firmwarepath}/iwlwifi-5000-*.ucode*
	
%{_firmwarepath}/iwlwifi-5150-*.ucode*
	
%{_firmwarepath}/iwlwifi-6000-*.ucode*
	
%{_firmwarepath}/iwlwifi-6000g2a-*.ucode*
	
%{_firmwarepath}/iwlwifi-6000g2b-*.ucode*
	
%{_firmwarepath}/iwlwifi-6050-*.ucode*
	
 
	
%files -n iwlwifi-mvm-firmware
	
%license LICENCE.iwlwifi_firmware
	
%{_firmwarepath}/iwlwifi-3160-*.ucode*
	
%{_firmwarepath}/iwlwifi-3168-*.ucode*
	
%{_firmwarepath}/iwlwifi-7260-*.ucode*
	
%{_firmwarepath}/iwlwifi-7265-*.ucode*
	
%{_firmwarepath}/iwlwifi-7265D-*.ucode*
	
%{_firmwarepath}/iwlwifi-8000C-*.ucode*
	
%{_firmwarepath}/iwlwifi-8265-*.ucode*
	
%{_firmwarepath}/iwlwifi-9000-*.ucode*
	
%{_firmwarepath}/iwlwifi-9260-*.ucode*
	
%{_firmwarepath}/iwlwifi-cc-a0-*.ucode*
	
%{_firmwarepath}/iwlwifi-gl-c0*
	
%{_firmwarepath}/iwlwifi-ma-b0*
	
%{_firmwarepath}/iwlwifi-Qu*.ucode*
	
%{_firmwarepath}/iwlwifi-ty-a0*
	
%{_firmwarepath}/iwlwifi-so-a0*
	
%{_firmwarepath}/iwlwifi-bz-b0*
	
 
	
%files -n libertas-firmware
	
%license LICENCE.Marvell LICENCE.OLPC
	
%dir %{_firmwarepath}/libertas
	
%dir %{_firmwarepath}/mrvl
	
%{_firmwarepath}/libertas/*
	
%{_firmwarepath}/mrvl/sd8787*
	
 
	
%files -n mt7xxx-firmware
	
%license LICENCE.mediatek
	
%license LICENCE.ralink_a_mediatek_company_firmware
	
%dir %{_firmwarepath}/mediatek
	
%{_firmwarepath}/mediatek/mt76*
	
%{_firmwarepath}/mediatek/mt79*
	
%{_firmwarepath}/mediatek/BT*
	
%{_firmwarepath}/mediatek/WIFI*
	
%{_firmwarepath}/mt76*
	
 
	
%files -n nxpwireless-firmware
	
%license LICENSE.nxp
	
%dir %{_firmwarepath}/nxp
	
%{_firmwarepath}/nxp/*
	
 
	
%files -n realtek-firmware
	
%license LICENCE.rtlwifi_firmware.txt
	
%{_firmwarepath}/rtl_bt/
	
%{_firmwarepath}/rtlwifi/
	
%{_firmwarepath}/rtw88/
	
%{_firmwarepath}/rtw89/
	
 
	
%files -n tiwilink-firmware
	
%license LICENCE.ti-connectivity
	
%dir %{_firmwarepath}/ti-connectivity/
	
%{_firmwarepath}/ti-connectivity/*
	
 
	
# SMART NIC and network switch firmwares
	
%files -n liquidio-firmware
	
%license LICENCE.cavium_liquidio
	
%dir %{_firmwarepath}/liquidio
	
%{_firmwarepath}/liquidio/*
	
 
	
%files -n mrvlprestera-firmware
	
%license LICENCE.Marvell
	
%dir %{_firmwarepath}/mrvl/prestera
	
%{_firmwarepath}/mrvl/prestera/*
	
 
	
%files -n mlxsw_spectrum-firmware
	
%dir %{_firmwarepath}/mellanox/
	
%{_firmwarepath}/mellanox/*
	
 
	
%files -n netronome-firmware
	
%license LICENCE.Netronome
	
%dir %{_firmwarepath}/netronome
	
%{_firmwarepath}/netronome/*
	
 
	
%files -n qed-firmware
	
%dir %{_firmwarepath}/qed
	
%{_firmwarepath}/qed/*
	
 
	
# Silicon Vendor specific
	
%files -n qcom-firmware
	
%license LICENSE.qcom LICENSE.qcom_yamato qcom/NOTICE.txt
	
%dir %{_firmwarepath}/qcom
	
%{_firmwarepath}/qcom/*
	
%{_firmwarepath}/a300_p*
	
 
	
# Vision and ISP hardware
	
%files -n intel-vsc-firmware
	
%license LICENSE.ivsc
	
%dir %{_firmwarepath}/intel/ipu/
	
%dir %{_firmwarepath}/intel/vsc/
	
%{_firmwarepath}/intel/ipu3-fw.bin*
	
%{_firmwarepath}/intel/irci_irci_ecr-master_20161208_0213_20170112_1500.bin*
	
%{_firmwarepath}/intel/ipu/*
	
%{_firmwarepath}/intel/vsc/*
	
 
	
# Sound codec hardware
	
%files -n cirrus-audio-firmware
	
%license LICENSE.cirrus
	
%dir %{_firmwarepath}/cirrus
	
%{_firmwarepath}/cirrus/*
	
 
	
%files -n intel-audio-firmware
	
%license LICENCE.adsp_sst LICENCE.IntcSST2
	
%dir %{_firmwarepath}/intel/
	
%dir %{_firmwarepath}/intel/avs/
	
%dir %{_firmwarepath}/intel/catpt/
	
%{_firmwarepath}/intel/avs/*
	
%{_firmwarepath}/intel/catpt/*
	
%{_firmwarepath}/intel/dsp_fw*
	
%{_firmwarepath}/intel/fw_sst*
	
 
	
# Random other hardware
	
%files -n dvb-firmware
	
%license LICENSE.dib0700 LICENCE.it913x LICENCE.siano
	
%license LICENCE.xc4000 LICENCE.xc5000 LICENCE.xc5000c
	
%dir %{_firmwarepath}/av7110/
	
%{_firmwarepath}/av7110/*
	
%{_firmwarepath}/as102_data*
	
%{_firmwarepath}/cmmb*
	
%{_firmwarepath}/dvb*
	
%{_firmwarepath}/isdbt*
	
%{_firmwarepath}/lgs8g75*
	
%{_firmwarepath}/sms1xxx*
	
%{_firmwarepath}/tdmb*
	
%{_firmwarepath}/v4l-cx2*
	
 
	
%changelog
