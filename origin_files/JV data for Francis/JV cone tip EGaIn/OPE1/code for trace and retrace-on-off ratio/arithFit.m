function [mf,sf,cf] = arithFit(l,runs)

    mf = mean(l);
    sf = std(l);
    z = 1.96*std(l)/(sqrt(runs*21));
    cf = [mf - z; mf + z];
            
end