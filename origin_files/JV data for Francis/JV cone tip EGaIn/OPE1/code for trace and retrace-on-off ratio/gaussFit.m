function [mf,sf,cf] = gaussFit(x,l,bins,plots)

    [h,xx] = histcounts(l,bins);
    %[h,xx] = histcounts(l,'BinMethod','scott'); 
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
        text(min(dx)+min(dx)*1/8,max(h)*7/8.,['mu = ', num2str(mf)]);
        text(min(dx)+min(dx)*1/8,max(h)*6.7/8.,['sig = ', num2str(sf)]);
        text(min(dx)+min(dx)*1/8,max(h)*6.5/8,['95 = ', num2str(cf)]);
    end
    
end