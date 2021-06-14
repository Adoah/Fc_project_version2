function rr = findRR(m)

    v = m.data(:,1);
    j = m.data(:,2);

    u = unique(abs(v));
    for i=1:length(u)
        if u(i) == 0
            f = find(v == 0);
            fp = f(2:3:end);
            fn = f(3:3:end);
        end
        if u(i) ~= 0
            fp = find(v == u(i));
            fn = find(v == -u(i));
%             if length(fp) ~= length(fn)
%                fp = fp(1:length(fn)); 
%             end
            if length(fp) < length(fn)
                fn = fn(1:length(fp));
            elseif length(fp) > length(fn)
                fp = fp(1:length(fn));
            end
        end
    rr{i} = log10(j(fn) ./ j(fp)); % neg / pos
    %rr{i} = log10(j(fp) ./ j(fn)); % pos / neg
       
    end
end