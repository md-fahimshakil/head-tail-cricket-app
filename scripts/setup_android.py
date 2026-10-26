import glob, os, shutil
R = 'android/app/src/main/'
m = open(R + 'AndroidManifest.xml', encoding='utf-8').read()
m = m.replace('<activity', '<activity android:screenOrientation="portrait"', 1)
f = '''<intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />
    <data android:scheme="com.ajairagames.headtailcricket" android:host="login" />
</intent-filter>
'''
m = m.replace('</activity>', f + '</activity>', 1)
open(R + 'AndroidManifest.xml', 'w', encoding='utf-8').write(m)
for d in ['mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi']:
    for n in ('ic_launcher.png', 'ic_launcher_round.png', 'ic_launcher_foreground.png'):
        shutil.copy('resources/icons/%s.png' % d, R + 'res/mipmap-%s/%s' % (d, n))
for x in glob.glob(R + 'res/mipmap-anydpi-v26/ic_launcher*.xml'):
    os.remove(x)
print('android project customised')
