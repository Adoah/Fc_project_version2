% This code was developed to take any IV data set that has a Vmax>0 and
% Vmin<0 taken in one continuous sweep using the labview codes isntalled on
% the Lab5 probestation and both EGaIn setups, Lab3 optical microscope and
% cleanroom probestation. 
% The code produces: IV, Log10 current density with log-normal errors,
% dI/dV and a Fowler-Nordheim plot. The latter two are produce with the
% average of the IV. 
%
% There are two different working datasets: onetrace and twotrace. 
% - onetrace is the complete averaged IV
% - twotrace is bias dependent to expose any hysteresis 
% 
% The code first analyses the input data (using readIn) and then plots the
% data (using ivPlots). Refrain from editting the readIn file on your
% machine unless you are very familiar with matlab -- it is quite complex
% and not heavily commented. However, ivPlots can be editted to your hearts
% content as this file may have large aesthetic preferences from user to
% user. ivPlots is heavily commented!
%
% This code only works if IV is swept in both directions!
%
% -- Thorin Jake Duffin, May 2017

clear all % Resets memory and any variables

fL = 'C:\Users\Ziyu\OneDrive - National University of Singapore\Research\Data\J-V\FcOPE3CSH 20190203\'; % This string should be the directory address to the text file

%%% Write text file name here

 f1 = '1.txt';%OK
 f2 = '2.txt';
 f3 = '3.txt';%OK
 f4 = '4.txt';
 f5 = '5.txt';%OK
 f6 = '6.txt';
 f7 = '7.txt';%OK
 f8 = '8.txt';
 f9 = '9.txt';
 f10 = '10.txt';%OK
 f11 = '11.txt';
 f12 = '12.txt';%OK
 f13 = '13.txt';
 f14 = '14.txt';%OK
 f15 = '15.txt';
 f16 = '16.txt';%OK
 f17 = '17.txt';
 f18 = '18.txt';
 f19 = '19.txt';%OK
 f20 = '20.txt';



% Add all text files you want to average
f = cellstr({f1;f2;f3;f4;f5;f6;f7;f8;f9;f10;f11;f12;f13;f14;f15;f16;f17;f18;f19;f20});
%f
%=cellstr({f1;f2;f3;f4;f5;f6;f7;f8;f9;f10;f11;f12;f13;f14;f15;f16;f17;f18;f19});
%%MATLAB2016

v = [-0.5, -0.4, -0.3];

[twotrace,onetrace] = readIn(fL,f); % Execute readIn script, return single and double trace data

%find(v)

ivPlots(twotrace,0) % Plot double trace data 
%ivPlots(onetrace,1) % Plot single trace data
