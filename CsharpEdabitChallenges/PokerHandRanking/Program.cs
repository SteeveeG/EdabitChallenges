using PokerHandRankingChallenge;
//Link to Cahllenge : https://edabit.com/challenge/MnPogX5KgggaRpaJo
 
var combinations = new List<string[]>();
combinations.Add(new[] {"10h", "Jh", "Qh", "Ah", "Kh" });
combinations.Add(new[] {"3h", "5h", "Qs", "9h", "Ad" });
combinations.Add(new[] {"10s", "10c", "8d", "10d", "10h" });
combinations.Add(new[] {"4h", "9s", "2s", "2d", "Ad" });
combinations.Add(new[] {"10s", "9s", "8s", "6s", "7s" });
combinations.Add(new[] {"10c", "9c", "9s", "10s", "9h" });
combinations.Add(new[] {"8h", "2h", "8s", "3s", "3c" });
combinations.Add(new[] {"Jh", "9h", "7h", "5h", "2h" });
combinations.Add(new[] {"Ac", "Qc", "As", "Ah", "2d" });
combinations.Add(new[] {"Ad", "Kd", "Qd", "Jd", "9d" });
combinations.Add(new[] {"10h", "Jh", "Qs", "Ks", "Ac" });
combinations.Add(new[] {"3h", "8h", "2s", "3s", "3d" });
combinations.Add(new[] {"4h", "Ac", "4s", "4d", "4c" });
combinations.Add(new[] {"3h", "8h", "2s", "3s", "2d" });
combinations.Add(new[] {"8h", "8s", "As", "Qh", "Kh" });
combinations.Add(new[] {"Js", "Qs", "10s", "Ks", "As" });
combinations.Add(new[] {"Ah", "3s", "4d", "Js", "Qd" });


foreach (var combination in combinations)
{
    var controlHand = new ControlHand(combination);
    Console.WriteLine(controlHand.StartControlHands());
}