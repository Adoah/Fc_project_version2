function [mf,sf,cf] = arithFit(l,runs)

    mf = mean(l);
    sf = std(l);
    z = 1.96*std(l)/sqrt(runs);
    cf = [mf - z; mf + z];
            
end