function [] = ivPlots(l,n)

    % This function accepts two variables: l, n
    % l is a dataset
    % n is an enumeration that is used to name the plot canvas
    %
    % - Thorin Jake Duffin, May 2017

    fs = 18;
    color = 'black';
    
    [v,mj,sj,cj,dx,dj,mc,sc,cc,hc,bc] = l{:}; % Extract all data from the list
    
    % Variables:
    % v - voltage
    % mj - mean current
    % sj - one sigma current
    % cj - 95 confidence current
    % dx - derivative of voltage
    % dj - derivative of current
    % mc - mean current density
    % sc - one sigma current density
    % cc - 95 confidence current density
    % hc - heatmap of current density
    % binsc - bins for heatmap

    % find current scale (mA, uA, nA, etc
    un = floor(log10(max(abs(mj)))/3)*3;
    
    % rescale current so it plots with the right y axis
    mj = mj./(10^un);
    sj = sj./(10^un);
    cj = cj./(10^un);
    dj = dj./(10^un);
    
    % scale y text according to rescaled current
    if un == 0
        sca = 'A';
    elseif un == -3
        sca = 'mA';
    elseif un == -6
        sca = '{\mu}A';
    elseif un == -9
        sca = 'nA';
    elseif un == -12
        sca = 'pA';
    elseif un == -15
        sca = 'fA';
    end
        
    
    
    figure(1001+n*7) % names the canvas

    % Average IV plot with error
    errorbar(v,mj,sj,'color',color); % plots with errorbars (x,y, errorbar)
    title('Average IV with error bars'); % title
    xlabel('voltage \it V \rm (V)', 'FontName', 'Arial', 'FontSize', 24); % x axis label
    ylabel(['current \it I \rm (' sca ')'], 'FontName', 'Arial', 'FontSize', 24); % y axis label
    set(gca, 'FontName', 'Arial', 'FontSize', fs); % axes label and fontsize
    set(gcf, 'renderer', 'opengl'); % improves the plot quality
    grid on; % grid lines
    
    figure(1002+n*7)
    
    % Average IV with 95% confidence
    plot(v,mj,'color',color);
    hold on; % allows multiple plots without erasing previous
    fill([v,fliplr(v)],[cj(1,:),fliplr(cj(2,:))],'b'); % fill space between two lines with color 'b'
    alpha(0.25); % transparency setting
    hold off; % plotting finished
    title('Average IV with 95% confidence')
    xlabel('voltage \it V \rm (V)', 'FontName', 'Arial', 'FontSize', 24);
    ylabel('J \rm (A/cm^2)', 'FontName', 'Arial', 'FontSize', 24);
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    grid on

    figure(1003+n*7)
    % Current density 
    errorbar(v,mc,sc,'color',color);
    title('current density');
    xlabel('voltage (V)', 'FontName', 'Arial', 'FontSize', 24);
    ylabel(['log_{10} |\it J \rm| (A/cm^2)'], 'FontName', 'Arial', 'FontSize', 24);
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    grid on
    
    figure(1004+n*7)
    hf = length(v) / 2 + 2;
    % Average IV with 95% confidence
    plot(v,mc,'color',color);
    hold on; % allows multiple plots without erasing previous
    %fill([v,fliplr(v)],[cc(1,:),fliplr(cc(2,:))],'b'); % fill space between two lines with color 'b'
    fill([v(1:hf),fliplr(v(1:hf))],[cc(1,1:hf),fliplr(cc(2,1:hf))],'b');
    fill([v(hf-1:end),fliplr(v(hf-1:end))],[cc(1,hf-1:end),fliplr(cc(2,hf-1:end))],'r');
    alpha(0.25); % transparency setting
    hold off; % plotting finished
    title('Average current density with 95% confidence')
    xlabel('voltage \it V \rm (V)', 'FontName', 'Arial', 'FontSize', 24);
    ylabel(['log_{10} |\it J \rm| (A/cm^2)'], 'FontName', 'Arial', 'FontSize', 24);
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    grid on
    
    figure(1005+n*7)
    % First deriv of average plot
    plot(dx,dj,'.','color',color);
    title('first derivative')
    xlabel('voltage \it V \rm (V)', 'FontName', 'Arial', 'FontSize', 24);
    ylabel(' d\itI\rm/d\itV \rm', 'FontName', 'Arial', 'FontSize', 24); 
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    grid on

    figure(1006+n*7)
    % Fowler-Nordheim Plot
    fx = 1./v;
    fy = log(abs(mj./(v.*v)));
    plot(fx,fy,'color',color)
    title('fowler-nordheim')
    xlabel('\it 1/V \rm (V^{-1})', 'FontName', 'Arial', 'FontSize', 24);
    ylabel(' ln(\itI/V^2 \rm)', 'FontName', 'Arial', 'FontSize', 24); 
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    grid on
    
    figure(1007+n*7)
    % Current density heatmap
    %plot background
    ylims = [-9 0]; % define limits -- change these to change limits
    bg = zeros(length(ylims),length(v)); % make matrix of zeros)
    pcolor(v,ylims,bg); % plot background

    hold on
    pcolor(v,bc(2:end),hc);
    shading interp;
    colormap jet;
    hold on
    plot(v,mc,'color','k');
    xlabel('voltage (V)', 'FontName', 'Arial', 'FontSize', 24);
    ylabel(['log_{10} |\it J \rm| (A/cm^2)'], 'FontName', 'Arial', 'FontSize', 24);
    set(gca, 'FontName', 'Arial', 'FontSize', fs);
    set(gcf, 'renderer', 'opengl');
    c = colorbar;
    xlim([-1 1]);
    set(c,'FontSize',18);
    pbaspect([1 1 1])
    hold on
    
end