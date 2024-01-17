using MiserableParodyOfACalculator;
// Link to Challenge: https://edabit.com/challenge/u2j86CBJibQA5KzQp

Console.WriteLine("Miserable Parody of a Calculator");

Calculator calculator = new Calculator();
Console.WriteLine("Rechnung: 23+4                    , Ergebniss: " + calculator.Calculate("23+4"));
Console.WriteLine("Rechnung: 45-15                   , Ergebniss: " + calculator.Calculate("45-15"));
Console.WriteLine("Rechnung: 13+2-5*2                , Ergebniss: " + calculator.Calculate("13+2-5*2"));
Console.WriteLine("Rechnung: 49/7*2-3                , Ergebniss: " + calculator.Calculate("49/7*2-3"));
Console.WriteLine("Rechnung: 2+2*2                   , Ergebniss: " + calculator.Calculate("2+2*2"));
Console.WriteLine("Rechnung: 5/2                     , Ergebniss: " + calculator.Calculate("5/2"));
Console.WriteLine("Rechnung: -34/4                   , Ergebniss: " + calculator.Calculate("-34/4"));
Console.WriteLine("Rechnung: 0+43-0+56*0             , Ergebniss: " + calculator.Calculate("0+43-0+56*0"));
Console.WriteLine("Rechnung: -14*2-37-0              , Ergebniss: " + calculator.Calculate("-14*2-37-0"));
Console.WriteLine("Rechnung: 0*0                     , Ergebniss: " + calculator.Calculate("0*0"));
Console.WriteLine("Rechnung: 4+2+3-5*2-8/4-12-0+3-14 , Ergebniss: " + calculator.Calculate("4+2+3-5*2-8/4-12-0+3-14"));
Console.WriteLine("Rechnung: 9/2+9/4                 , Ergebniss: " + calculator.Calculate("9/2+9/4"));
Console.WriteLine("Rechnung: 56*27*18*12/2*0         , Ergebniss: " + calculator.Calculate("56*27*18*12/2*0"));
Console.WriteLine("Rechnung: 34/4*0*45*7             , Ergebniss: " + calculator.Calculate("34/4*0*45*7"));

Console.ReadKey();