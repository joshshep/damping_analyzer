clc
clear

% functions used
% function [y,t] = tfSine(a ,wn, z, x0, xdot0, steptime, endtime)
% function [y,t] = tfStep(a ,wn, z, x0, xdot0, steptime, endtime)

% magnitude
mag = 1;

% define array for frequency
f = [0.5 1 1.5 2 2.5 3 3.3 4 5 8];
wn = 2*pi*f;
l_wn = length(wn);

% define arrays for damping ratio
zeta = [0 0.05 0.2 0.5 0.8];
l_zeta = length(zeta);

for i = 1:l_wn
    figure('units','normalized','outerposition',[0 0 1 1])
    for j = 1:l_zeta
        [y,t] = tfStep(mag, wn(i), zeta(j), 0, 0, 0.01, 10);
        plot(t,y,'DisplayName', ['Frequency:' num2str(f(i)) ', Magnitude: ' num2str(mag) ', Damping Ratio: ' num2str(zeta(j))])
        grid on
        hold on
    end
    
    ylabel('Magnitude')
    xlabel('Time (sec)')
    legend('show');
        
    hold off
end

