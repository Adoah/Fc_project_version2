function [twotrace,onetrace] = readIn(dir,filename,plots)
    mv=[];
    mj=[];
    mc=[];
    for n=1:length(filename)

        % Import data from raw file
        df1 = importdata(char(strcat(dir,filename(n)))); % read in file

        % Extract data
        v = df1.data(:,1); % voltage
        j = df1.data(:,5); % current
        c = df1.data(:,3); % current density

        % Find the zeroes

        [valax,posax] = max(v);
        [valin,posin] = min(v);
        whereZ = find(v==0,3);

        % Finds zeroes for whether code has 2 or 3 recorded zeroes per sweep

        if(posin > whereZ(2))
            L = whereZ(3)-whereZ(1) + 1;
        else
            L = whereZ(2)-whereZ(1) + 1;
        end

        % Calculates the number of runs by dividing number of zeroes by the
        % length of the list

        runs = length(v)/L;

        % Make sure runs is an integer and reshape data so tha each row is a
        % single sweep
    
        if(rem(runs,1) == 0)
            mv0 = reshape(v,[L,runs]);
            mj0 = reshape(j,[L,runs]);
            mc0 = reshape(c,[L,runs]);
        end
        
        mv = [mv mv0];
        mj = [mj mj0];
        mc = [mc mc0];
    end


    % Front bias -- back bias
    mv2 = mv([posin:end,1:posin-1],:);
    mj2 = mj([posin:end,1:posin-1],:);
    mc2 = mc([posin:end,1:posin-1],:);
    
    % Number of bins
    bins = floor(sqrt(length(mj2)));
    
 
    
    %%% Separating forward and backward bias
    
    % x for two traces
    vx = mv2(:,1)';

    % Get mean and error
    for i=1:L
        try % First try gaussian fit
            [mfj(i),sfj(i),cfj(:,i)] = gaussFit(vx(i),mj2(i,:)',bins,0); % current
            [mfc(i),sfc(i),cfc(:,i)] = gaussFit(vx(i),log10(abs(mc2(i,:)')),bins,0); % current density
        catch % Gaussian fit fails to converge, use mathematical
            warning('Problem finding gaussian mean.  Computing arithmetic mean instead.');
            % arithmetic fit
            [mfj(i),sfj(i),cfj(:,i)] = arithFit(mj2(i,:),runs); % current
            [mfc(i),sfc(i),cfc(:,i)] = arithFit(log10(abs(mc2(i,:))),runs); % current density
        end
    end

    % First derivative data
    d1v = vx';
    [dval,dmax] = max(d1v);
    d1mf1 = diff(mfj(1:dmax-1));
    d1mf2 = diff(fliplr(mfj(dmax-1:end)));
    d1fvx = [d1v(2:dmax-1); flipud(d1v(dmax-1:end-1))];
    d1fm = [d1mf2 d1mf2];
    
    %%% Averaging together forwards and backwards bias
    
    % x for full average 
    uv = unique(mv2);

    % Get mean and error
    for i=1:length(uv)
        ff = find(mv2==uv(i));   
        try
            [maj(i),saj(i),caj(:,i)] = gaussFit(mj2(ff)',bins); % current
            [mac(i),sac(i),cac(:,i)] = gaussFit(log10(abs(mc2(i,:)')),bins); % current density
        catch %'Error using fit>iFit'
            warning('Problem finding gaussian mean.  Computing arithmetic mean instead.');
            [maj(i),saj(i),caj(:,i)] = arithFit(mj2(ff),bins); % current
            [mac(i),sac(i),cac(:,i)] = arithFit(log10(abs(mc2(i,:))),runs); % current density
        end
    end

    % First derivative data
    d1am = diff(maj);
    d1avx = uv(1:end-1);
    
    % Make heatmap data
    
    binNoj = bins;
    binNoc = 100;
    tMinj = min(min(mj2));
    tMaxj = max(max(mj2));
    tMinc = min(min(log10(abs(mc2))));
    tMaxc = max(max(log10(abs(mc2))));
    binsj = linspace(tMinj,tMaxj,binNoj);
    binsc = linspace(tMinc,tMaxc,binNoc);
    
    for i=1:L
        histj = histcounts(mj2(i,:)',binsj);% current
        heatj(:,i) = histj';
        [histc, bc] = histcounts(log10(abs(mc2(i,:)))',binsc);  % current density
        heatc(:,i) = histc';
    end

    %%% Export all data
    twotrace = {vx,mfj,sfj,cfj,d1fvx,d1fm,mfc,sfc,cfc,heatc,bc};
    onetrace = {uv',maj,saj,caj,d1avx,d1am,mac,sac,cac};
    
end