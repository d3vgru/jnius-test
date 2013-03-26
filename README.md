# Setup
- clone kivy/python-for-android
- ./distribute.sh -m kivy
- copy java/org/renpy/android to dist/default/src/org/renpy/android (this adds a static log method to the beginning of the activity source)
- build apk
# Results
- something like
	I/DEBUG   (26958): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
	I/DEBUG   (26958): Build fingerprint: 'ZTE/ZTE_Fury/sean:2.3.6/GINGERBREAD/20120831.044502:user/release-keys'
	I/DEBUG   (26958): pid: 29841, tid: 29866  >>> org.renpy.android:python <<<
	I/DEBUG   (26958): signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 00000038
- fault addr will always be 00000038
- stack trace
	I/DEBUG   (26958):          #00  pc 00047d04  /system/lib/libdvm.so
	I/DEBUG   (26958):          #01  pc 0004bca0  /system/lib/libdvm.so
	I/DEBUG   (26958):          #02  pc 0001ad78  /system/lib/libdvm.so
	I/DEBUG   (26958):          #03  pc 0004bd22  /system/lib/libdvm.so
	I/DEBUG   (26958):          #04  pc 0004bb18  /system/lib/libdvm.so
	I/DEBUG   (26958):          #05  pc 0004bb90  /system/lib/libdvm.so
	I/DEBUG   (26958):          #06  pc 000434e6  /system/lib/libdvm.so
	I/DEBUG   (26958):          #07  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #08  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #09  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #10  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #11  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #12  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #13  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #14  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #15  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #16  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #17  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #18  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #19  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #20  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #21  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #22  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #23  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #24  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #25  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #26  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #27  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #28  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #29  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #30  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
	I/DEBUG   (26958):          #31  pc 0014727c  /data/data/org.renpy.android/files/libpymodules.so
- 00047d04 in libdvm.so = dvmAddToReferenceTable
- 0014727c in libpymodules.so = initjnius
- disabling either the call to PythonActivity.log() or thread.start() should avoid the crash
