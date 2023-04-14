% classdef stat_class
%     %STAT_CLASS Summary of this class goes here %   Detailed explanation
%     goes here
%     
%     properties
%         %sets default values of properties population=100
%         
%         
%         
%     end %use cell class inputs, or cell arrays, to input multiple
%     arguments, instead of using %*args like you would in python.
%     
%     
%     methods
%         function obj = stat_class(iput_data,inputArg2)
%             %STAT_CLASS Construct an instance of this class %   input a
%             cell array into the input_data. %   Cell array should
%             include:
%             
%             obj.Property1 = inputArg1 + inputArg2;
%         end
%         
%         function outputArg = method1(obj,inputArg)
%             %METHOD1 Summary of this method goes here %   Detailed
%             explanation goes here
            outputArg = obj.Property1 + inputArg;
        end
    end
end

