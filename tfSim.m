function [y,t] = tfSim(inputType, a, wn, z, x1, x2, steptime, endtime)

    num = [0,0,wn^2];
    den = [1,2*z*wn,wn^2];

    dt = 0:steptime:endtime;

    if(inputType == "sine")
        u = a*sin(2*pi*dt); 
    elseif(inputType == "step")
        u = a*ones(1,numel(dt));    
    else
        print("error: Invalid Input Type");
    end


    [A,B,C,D] = tf2ss(num,den);
    sys = ss(A, B, C, D);

    if(x1~=0)
        x1=x1/C(2);
    end
    if(x2~=0)
        x2=x2/C(2);
    end

    [y,t] = lsim(sys, u, dt, [x1; x2]);
end