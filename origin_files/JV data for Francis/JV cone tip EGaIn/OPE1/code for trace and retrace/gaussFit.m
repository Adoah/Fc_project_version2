function [mf,sf,cf] = gaussFit(x,l,bins,plots)

    %[h,xx] = histcounts(l,bins);
    [h,xx] = histcounts(l,'BinMethod','fd'); 
    dx = xx(1:end-1)+diff(xx)/2.;
    fo = fit(dx',h','gauss1');
    mf = fo.b1; % mean
    sf = fo.c1 / sqrt(2); % sigma
    co = confint(fo,0.95);
    cf = co(:,2);
    
    if plots == 1
        figure
        bar(dx, h)
        hold on
        plot(fo)
        xlabel('current density')
        title(sprintf(' %f V', x))
    end
    
end