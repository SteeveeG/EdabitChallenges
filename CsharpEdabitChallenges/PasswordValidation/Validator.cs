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

        if (upperCaseRegex.IsMatch(password))
        {
            return "Missing Numbers and lowercase";
        }
  
        if (lowerCaseRegex.IsMatch(password))
        {
            return "Missing Numbers and uppercase";
        }
        if (numbersRegex.IsMatch(password))
        {
            return "Missing lowercase and uppercase";
        }
        if (alphabeticRegex.IsMatch(password))
        {
            return "Missing Numbers";
        }
        if (numbersLowerCaseRegex.IsMatch(password))
        {
            return "Missing uppercase";
        }
        if (numbersUpperCaseRegex.IsMatch(password))
        {
            return "Missing lowercase";
        }
        if (!specialCharactersRegex.IsMatch(password))
        { 
            return "Special Character not Supported";
        }
        return password.Where((t, i) => t == password[(i + 1) % password.Length] &&
                                        t == password[(i + 2) % password.Length]).Any() ? "Maximum of 2 repeated characters" : "OK !";
    }
}