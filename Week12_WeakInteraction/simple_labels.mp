% simple_labels.mp -- do not edit, generated automatically by homework10_solutions.tex
input feynmp
require_RCS_revision "1.30";
beginchar(1, 110*1.0pt#, 60*1.0pt#, 0);
"feynmf: 1";
LaTeX_unitlength:=1.0pt;
subgraph (0, 0, w, h);
vinit;
pickup pencircle scaled thin;
vlabel ("$\bar {\nu }_\mu $", __i1);
vlabel ("p", __i2);
vlabel ("n", __o2);
vlabel ("$\mu ^+$", __o1);
vleft (__i1, __i2);
vright (__o1, __o2);
vconnect ("plain", __i1, __v1);
vconnect ("plain", __i2, __v1);
vconnect ("plain", __v1, __o2);
vconnect ("plain", __v1, __o1);
vdot (__v1);
vlabel (" $\sim \frac {1}{m_W^2}$", __v1);
vfreeze;
vdraw;
endsubgraph;
endchar;
% the end.
end.
endinput;
