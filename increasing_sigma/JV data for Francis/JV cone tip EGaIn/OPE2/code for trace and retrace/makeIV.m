clear all

fL = 'D:\HYM\analysis\BTTF 20170228 Au(1.5V)\'; % This string should be the directory address to the text file

%%% Text files listed below, comment out all that you don't want 

f =cellstr({f1});

df1 = importdata(strcat(fL,f));

v = df1.data(:,1);
j = df1.data(:,3);
c = df1.data(:,5);

[valax,posax] = max(v);
[valin,posin] = min(v);
whereZ = find(v==0,3);

if(posin > whereZ(2))
    L = whereZ(3)-whereZ(1) + 1;
else
    L = whereZ(2)-whereZ(1) + 1;
end

runs = length(v)/L;

if(rem(runs,1) == 0)
    mv = reshape(v,[L,runs]);
    mj = reshape(j,[L,runs]);
    mc = reshape(c,[L,runs]);
end

lv = length(mv);

% Front bias -- back bias

mv2 = mv([posin:end,1:posin-1],:);
mj2 = mj([posin:end,1:posin-1],:);
mc2 = mc([posin:end,1:posin-1],:);
bins = floor(sqrt(runs))-1;
for i=1:lv
    try
        [h,xx] = histcounts(mj2(i,:)',bins);
        dx = xx(1:end-1)+diff(xx)/2.;
        fo = fit(dx',h','gauss1');
        mf(i) = fo.b1; % mean
        sf(i) = fo.c1 / sqrt(2); % sigma
        co = confint(fo,0.95);
        cf(:,i) = co(:,2);
    catch %'Error using fit>iFit'
        warning('Problem finding gaussian mean.  Computing arithmetic mean instead.');
        mf(i) = mean(mj2(i,:));
        sf(i) = std(mj2(i,:));
        z = 1.96*std(mj2(i,:))/sqrt(runs);
        cf(:,i) = [mean(mj2(i,:)) - z; mean(mj2(i,:)) + z];
    end
end

vx = mv2(:,1)';
%[v,j,c] = readIn(fL,f);

% All IV curves
plot(mv2,mj2);

% Average IV Plot with error
errorbar(vx,mf,sf)

% Average IV with 95% confidence
plot(vx,mf)
hold on
fill([vx,fliplr(vx)],[cf(1,:),fliplr(cf(2,:))],'r')
alpha(0.25)

% Average IV with errors and 95% confidence
errorbar(vx,mf,sf);
hold on
fill([vx,fliplr(vx)],[cf(1,:),fliplr(cf(2,:))],'r')
alpha(0.25)

% First deriv of average plot
d1v = mv2(:,1);
[dval,dmax] = max(d1v);
d1mf1 = diff(mf(1:dmax-1));
d1mf2 = diff(fliplr(mf(dmax-1:end)));
d1vx = [d1v(2:dmax-1); flipud(d1v(dmax-1:end-1))];
d1mf = [d1mf2 d1mf2];
plot(d1vx,d1mf,'.')

% Fowler-Nordheim Plot

%%% Single averaged curve

uv = unique(mv2);

for i=1:length(uv)
    ff = find(mv2==uv(i));
    
    try
        [h,xx] = histcounts(mj2(ff)',bins); %line gives trouble
        dx = xx(1:end-1)+diff(xx)/2.;
        fo = fit(dx',h','gauss1');
        allmf(i) = fo.b1; % mean
        allsf(i) = fo.c1 / sqrt(2); % sigma
        co = confint(fo,0.95);
        allcf(:,i) = co(:,2);
    catch %'Error using fit>iFit'
        warning('Problem finding gaussian mean.  Computing arithmetic mean instead.');
        allmf(i) = mean(mj2(ff));
        allsf(i) = std(mj2(ff));
        zz = 1.96*std(mj2(ff))/sqrt(runs);
        allcf(:,i) = [mean(mj2(ff)) - zz; mean(mj2(ff)) + zz];
    end
end

% Average IV Plot with error
errorbar(uv,allmf,allsf);

% Average IV with 95% confidence
plot(uv,allmf)
hold on
fill([uv',fliplr(uv')],[allcf(1,:),fliplr(allcf(2,:))],'r')
alpha(0.25)

% Average IV with errors and 95% confidence
errorbar(uv,allmf,allsf);
hold on
fill([uv',fliplr(uv')],[allcf(1,:),fliplr(allcf(2,:))],'r')
alpha(0.25)

% First deriv of average plot
d1allmf = diff(allmf);
d1allv = uv;
plot(uv(1:end-1),d1allmf)

% Fowler-Nordheim Plot
fnx = 1./uv';
fny = log(abs(allmf./(uv'.*uv')));
plot(fnx,fny)