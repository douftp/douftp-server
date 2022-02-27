# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

datas = [
    # (os.path.join('src', 'data', 'image', 'logo_about.png'), 'data/image')
]
hiddenimports = [
    'pyftpdlib.authorizers', 'pyftpdlib.handlers', 'pyftpdlib.servers'
]

a = Analysis(
    ['src/douftpserver.py'],
    pathex=['src'],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz,
          a.scripts, [],
          exclude_binaries=True,
          name='DouFTP Server',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DouFTP Server')
app = BUNDLE(
    coll,
    name='DouFTP Server.app',
    # icon='resources/app.icns',
    bundle_identifier='org.douftp.server.desktop',
    info_plist={
        'CFBundleName': 'DouFTP Server',
        'CFBundleDisplayName': 'DouFTP Server 桌面端',
        'CFBundleGetInfoString': "Crogram Inc.",
        'CFBundleIdentifier': "org.douftp.server.desktop",
        'CFBundleVersion': "0.0.1",
        'CFBundleShortVersionString': "0.0.1",
        'CFBundleInfoDictionaryVersion': '0.0.1',
        'CFBundlePackageType': 'APPL',
        'CFBundleSupportedPlatforms': ['MacOSX'],
        'LSMinimumSystemVersion': '11.0', # 最低系统版本
        'NSHumanReadableCopyright': "Copyright © 2018-2022 Crogram Inc. All Rights Reserved.",
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities'
    })
