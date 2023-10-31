/*
 * -----------------------------------------------------------------------
 * Author: Saurabh Zinjad
 * Developer Email: zinjadsaurabh1997@gmail.com
 * File: q3_mentions.cs
 * Creation Time: Oct 30th 2023 11:32 pm
 * Copyright (c) 2023 Saurabh Zinjad. All rights reserved | GitHub: Ztrimus
 * -----------------------------------------------------------------------
 */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

class Program
{
    static HashSet<string> FindMentions(string text)
    {
        string pattern = @"@id(\d+)(?:,\s*id(\d+))*";
        var mentions = Regex.Matches(text, pattern)
                            .Cast<Match>()
                            .SelectMany(m => m.Groups.Cast<Group>().Skip(1).Select(g => "id" + g.Value));
        return new HashSet<string>(mentions);
    }

    static List<string> Solution(List<string> members, List<string> messages)
    {
        Dictionary<string, int> res = members.ToDictionary(member => member, member => 0);

        foreach (var msg in messages)
        {
            foreach (var mention in FindMentions(msg))
            {
                if (res.ContainsKey(mention))
                {
                    res[mention]++;
                }
            }
        }

        var sortedRes = res.OrderByDescending(x => x.Value).ThenBy(x => x.Key);

        return sortedRes.Select(pair => $"{pair.Key}={pair.Value}").ToList();
    }

    static void Main()
    {
        List<string> members = new List<string> { "id123", "id234", "id7", "id321" };

        List<string> messages = new List<string>
        {
            "Hey @id123,id321 review this PR please! @id123 what do you think",
            "Hey @id7 nice appro@ch! Great job! @id800 what do you think?",
            "@id123,id321 thx!"
        };

        List<string> result = Solution(members, messages);

        Console.WriteLine($"[{string.Join(", ", result)}]");
    }
}
