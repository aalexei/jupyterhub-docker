#!/bin/bash

# Install base Julia packages
julia -e '
import Pkg;
Pkg.update();
Pkg.add([
    "DataFrames",
    "IJulia",
    "Convex",
    "SCS",
    "COSMO",
    "LaTeXStrings",
    "Symbolics",
    "VegaLite",
    "QuantumOptics",
    "PastaQ",
    "ZXCalculus",
    "Yao",
    "YaoPlots",
    "ITensors",
]);
Pkg.precompile();
'

