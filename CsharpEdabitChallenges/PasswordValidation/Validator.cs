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
        return password.Length switch
        {
            > 24 => "too long",
            < 6 => "too short",
            _ => password switch
            {
                { } s when upperCaseRegex.IsMatch(password) => "Missing Numbers and lowercase",
                { } s when lowerCaseRegex.IsMatch(password) => "Missing Numbers and uppercase",
                { } s when alphabeticRegex.IsMatch(password) => "Missing Numbers",
                { } s when numbersRegex.IsMatch(password) => "Missing lowercase and uppercase",
                { } s when numbersLowerCaseRegex.IsMatch(password) => "Missing uppercase",
                { } s when numbersUpperCaseRegex.IsMatch(password) => "Missing lowercase",
                { } s when specialCharactersRegex.IsMatch(password) => "Special Character not Supported",
                _ => password.Where((t, i) => t == password[(i + 1) % password.Length] &&
                                              t == password[(i + 2) % password.Length])
                    .Any()
                    ? "Maximum of 2 repeated characters"
                    : "OK !"
            }
        };
    }
}