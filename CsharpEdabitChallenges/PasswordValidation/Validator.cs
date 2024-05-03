using System.Text.RegularExpressions;

namespace PasswordValidation;

public class Validator
{
    Regex upperCaseRegex = new("^[A-Z]+$");
    Regex lowerCaseRegex = new("^[a-z]+$");
    Regex alphabeticRegex = new("^[A-Za-z]+$");
    Regex numbersRegex = new("^[0-9]+$");
    Regex numbersLowerCaseRegex = new("^[a-z0-9]+$");
    Regex numbersUpperCaseRegex = new("^[A-Z0-9]+$");
    Regex specialCharactersRegex = new("^[a-zA-Z0-9!@#$%^&*()+=_-{}\\[\\]:;\"'<>?,.-]+$");
    


    public string ValidatePassword(string password)
    {
        switch (password.Length)
        {
            case > 24:
                return "too long";
            case < 6:
                return "too short";
        }

        switch (password)
        { 
            case { } s when upperCaseRegex.IsMatch(password):
                return "Missing Numbers and lowercase";
             case { } s when lowerCaseRegex.IsMatch(password):
                return "Missing Numbers and uppercase";
            case { } s when alphabeticRegex.IsMatch(password):
                return "Missing Numbers";
            case { } s when numbersRegex.IsMatch(password):
                return "Missing lowercase and uppercase";
            case { } s when numbersLowerCaseRegex.IsMatch(password):
                return "Missing uppercase";
            case { } s when numbersUpperCaseRegex.IsMatch(password):
                return "Missing lowercase";
            case { } s when specialCharactersRegex.IsMatch(password):
                return "Special Character not Supported";

        }
        return password.Where((t, i) => t == password[(i + 1) % password.Length] &&
                                        t == password[(i + 2) % password.Length]).Any() ? "Maximum of 2 repeated characters" : "OK !";
    }
}