import classical_force.*
clc
vector=[1,0,2];
disTAnce=get_distance(vector)
vector./disTAnce
x=0.6852+0.7809*0.7677+0.8944*1.2258
800/x
function [resultant,direction] = sum_forces(forces)
%forces is an array of class classical_forces
    forcematrix=NaN;
    for x = forces
        items=str2num(x) %#ok<ST2NM>;
        force=classical_force(items(1),items(2),"degrees");
        x_forces=x_forces+force.components(1);
        y_forces=y_forces+force.components(2);
    end
    resultant=sqrt((x_forces))^2+((y_forces)^2);
    direction=atand(y_forces/x_forces);
end

function [acceleration]= find_accel(force,mass)
    acceleration=force/mass;
end

function distance=get_distance(vector)
distance=sqrt(sum(vector.^2));
end
%%Verified using https://www.omnicalculator.com/math/vector-addition
