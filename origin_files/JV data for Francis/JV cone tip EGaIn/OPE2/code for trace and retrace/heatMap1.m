clear all

fL = 'E:\Viologen\MeV2+C11SH 2cl- 20180417\';


files = dir(strcat(fL,'*.txt')); %list files

% make a list of the files
for i = 1:length(files) 
   a(i) = importdata(strcat(fL,files(i).name));
   mi(i) = min(a(i).data(:,2));
   ma(i) = max(a(i).data(:,2));
end

%tMin = min(mi);
%tMax = max(ma);
tMin = log10(min(mi));
tMax = log10(max(ma));
tMaAve = mean(ma);
binNo = 30;

bins = linspace(tMin,tMax,binNo);

x = unique(a(1).data(:,1));
%h = zeros(length(bins)-1,length(x)); % matlab2014
h = zeros(length(bins),length(x)); % matlab2011

for j = 1:length(x)
    for i = 1:length(a) 
        f = find(a(i).data(:,1) == x(j));
        %aa = a(i).data(f,2);
        aa = log10(a(i).data(f,2));
%         h(:,j)=h(:,j)+transpose(histcounts(aa,bins)); % matlab2014
        N = transpose(hist(aa,bins)); % matlab2011
        h(:,j)=h(:,j)+N; % matlab2011
        aveA(j) = mean(aa);
        stdA(j) = std(aa);
        
    end
end

%b = mean([bins(1:end-1);bins(2:end)]);% matlab2014
b = bins; % matlab2011

for i = 1:length(a)
   if i == 1
       rr = findRR(a(i));
   else
       rr = [rr;findRR(a(i))]; 
   end
end

[rx,ry] = size(rr);

for i = 1:rx
    for j = 1:ry
        rma(i,j) = max(rr{i,j});
        rmi(i,j) = min(rr{i,j});
    end
end

rmax = max(max(rma));
rmin = min(min(rmi));

rMin = rmin;
rMax = rmax;
rbinNo = 30;

rbins = linspace(rMin,rMax,rbinNo);
%rb = mean([rbins(1:end-1);rbins(2:end)]); % matlab2014
rb = rbins; % matlab2011
%rh = zeros(length(rbins)-1,ry); % matlab2014
rh = zeros(length(rbins),ry);
rxx = unique(abs(a(1).data(:,1)));

for j = 1:ry
    for i = 1:rx
        if i == 1
            hi = rr{i,j};
        else
            hi = [hi;rr{i,j}];
        end
    end
    rN = transpose(hist(hi,rbins)); % matlab2011
    %rh(:,j)=rh(:,j)+transpose(histcounts(hi,rbins)); % matlab2014
    rh(:,j) = rh(:,j) + rN; % matlab2011
    averA(j) = mean(hi);
    stdrA(j) = std(hi);
end

h = h/2.;
rh = rh/2.;



figure(1)

%plot background
ylims = [-10 2]; % define limits -- change these to change limits
bg = zeros(length(ylims),length(x)); % make matrix of zeros)
pcolor(x,ylims,bg); % plot background

hold on

pcolor(x,b,h);
shading interp;
colormap jet;
xlabel('\it V \rm (V)', 'FontName', 'Arial', 'FontSize', 18);
ylabel('log_{10}|\itJ\rm| (A/cm^2)', 'FontName', 'Arial', 'FontSize', 18); 
set(gca, 'FontName', 'Arial', 'FontSize', 18);
set(gca, 'XTick',[-3:1:3]); %set X tick
set(gca, 'XTickLabel', [-3:1:3]); % set X tick
set(gcf, 'renderer', 'opengl');
c = colorbar;
set(c,'FontSize',18);
pbaspect([1 1 1])
%caxis([-60.0, 0]);
hold on

%errorbar(x,aveA,stdA,'k')

hold off

figure(2)

%plot background
ylims = [-2 8]; % define limits -- change these to change limits
bg = zeros(length(ylims),length(x)); % make matrix of zeros)
pcolor(x,ylims,bg); % plot background

hold on

pcolor(rxx,rb,rh);
shading interp;
colormap jet;
xlabel('\it V \rm (V)', 'FontName', 'Arial', 'FontSize', 18);
ylabel('log_{10}\itR', 'FontName', 'Arial', 'FontSize', 18); 
set(gca, 'FontName', 'Arial', 'FontSize', 18);
set(gcf, 'renderer', 'opengl');
c = colorbar;
xlim([0 1.3]);
set(c,'FontSize',18);
pbaspect([1 1 1])
hold on

%errorbar(rxx,averA,stdrA,'k')