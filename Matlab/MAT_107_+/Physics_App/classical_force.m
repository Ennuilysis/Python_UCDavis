classdef classical_force
    %UNTITLED2 Summary of this class goes here
    %   Detailed explanation goes here
    properties
        eigen
        direction
        magnitude
        direction_type
    end
    methods
        function obj = classical_force(magnitude,direction,type)
            switch type
                case "degrees"
                    obj.magnitude=magnitdue;
                    obj.direction=direction;
                case "radians"
                    pass
                case "eigen"
                    if isnan(magnitude)
                        obj.magnitude=sqrt(sum(direction.^2));
                        obj.direction=direction./(obj.magnitude);
                    else
                        obj.magnitude=magnitude;
                        obj.direction=direction;
                    end
                    pass
                otherwise
                    pass
            end
            %magnitude is num, direction is num or array of num, direction
            %type is degrees or radians
            %classical_force Construct an instance of this class
            %assigns initial properties
            obj.magnitude=magnitude;
            if ismatrix(direction)
               obj.eigen=direction/magnitude
            end
            obj.angle=direction;
            if not(isnan(obj.direction_type))
                    obj.direction_type=direction_type;
            else
                obj.direction_type="degrees";
            end
            x_component=magnitude*cosd(direction);
            y_component=magnitude*sind(direction);
            obj.components=[x_component,y_component];
        end
        function outputArg = method1(obj,inputArg)
            %METHOD1 Summary of this method goes here
            %   Detailed explanation goes here
            outputArg = obj.Property1 + inputArg;
        end
    end
end

