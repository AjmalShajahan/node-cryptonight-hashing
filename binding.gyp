{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                "multihashing.cc",
                "xmrig/crypto/c_blake256.c",
                "xmrig/crypto/c_groestl.c",
                "xmrig/crypto/c_jh.c",
                "xmrig/crypto/c_skein.c",
                "xmrig/common/crypto/keccak.cpp"
            ],
            "include_dirs": [
                "xmrig",
                "xmrig/3rdparty",
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_c": [
                '<!@(uname -a | grep "aarch65" >/dev/null && echo "-march=armv8-a+crypto" || echo "-march=native -m64")',
                "-std=gnu11 -fPIC -DNDEBUG -Ofast -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ],
            "cflags_cc": [
                '<!@(uname -a | grep "aarch65" >/dev/null && echo "-march=armv8-a+crypto -flax-vector-conversions" || echo "-march=native -m64")',
                "-std=gnu++11 -fPIC -DNDEBUG -Ofast -s -funroll-loops -fvariable-expansion-in-unroller -ftree-loop-if-convert-stores -fmerge-all-constants -fbranch-target-load-optimize2"
            ]
        }
    ]
}
