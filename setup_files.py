import os
import json

CONTENT_DIR = "content"
os.makedirs(CONTENT_DIR, exist_ok=True)

# 1. Virginia Plan (May 29, 1787)
virginia_plan = """1. Resolved that the Articles of Confederation ought to be so corrected & enlarged as to accomplish the objects proposed by their institution; namely, "common defence, security of liberty and general welfare."

2. Resolved therefore that the rights of suffrage in the National Legislature ought to be proportioned to the Quotas of contribution, or to the number of free inhabitants, as the one or the other rule may seem best in different cases.

3. Resolved that the National Legislature ought to consist of two branches.

4. Resolved that the members of the first branch of the National Legislature ought to be elected by the people of the several States every [term] years...

5. Resolved that the members of the second branch of the National Legislature ought to be elected by those of the first, out of a proper number of persons nominated by the individual Legislatures...

6. Resolved that each branch ought to possess the right of originating Acts; that the National Legislature ought to be impowered to enjoy the Legislative Rights vested in Congress by the Confederation & moreover to legislate in all cases to which the separate States are incompetent...

7. Resolved that a National Executive be instituted; to be chosen by the National Legislature for the term of [term] years...

8. Resolved that the Executive and a convenient number of the National Judiciary, ought to compose a Council of revision with authority to examine every act of the National Legislature before it shall operate...

9. Resolved that a National Judiciary be established to consist of one or more supreme tribunals, and of inferior tribunals to be chosen by the National Legislature...

10. Resolved that provision ought to be made for the admission of States lawfully arising within the limits of the United States...

11. Resolved that a Republican Government & the territory of each State... ought to be guaranteed by the United States to each State.

12. Resolved that provision ought to be made for the continuance of Congress... until a given day after the reform of the articles of Union shall be adopted...

13. Resolved that provision ought to be made for the amendment of the Articles of Union whensoever it shall seem necessary...

14. Resolved that the Legislative Executive & Judiciary powers within the several States ought to be bound by oath to support the articles of Union.

15. Resolved that the amendments which shall be offered to the Confederation, by the Convention ought at a proper time, or times, to be submitted to an assembly or assemblies of Representatives, recommended by the several Legislatures to be expressly chosen by the people, to consider & decide thereon.
"""

with open(os.path.join(CONTENT_DIR, "Draft_1_Virginia_Plan.md"), "w") as f:
    f.write(virginia_plan)

# 2. Committee of Detail (August 6, 1787) - Abridged for key structure
committee_detail = """We the People of the States of New-Hampshire, Massachusetts, Rhode-Island and Providence Plantations, Connecticut, New-York, New-Jersey, Pennsylvania, Delaware, Maryland, Virginia, North-Carolina, South-Carolina, and Georgia, do ordain, declare and establish the following Constitution for the Government of Ourselves and our Posterity.

ARTICLE I
The stile of this Government shall be, "The United States of America."

ARTICLE II
The Government shall consist of supreme legislative, executive and judicial powers.

ARTICLE III
The legislative power shall be vested in a Congress, to consist of two separate and distinct bodies of men, a House of Representatives, and a Senate...

[...Detailed Articles IV - XXIII describing the powers, election processes, and restrictions...]

ARTICLE XXIII
The ratification of the Conventions of ______ States shall be sufficient for organizing this Constitution.
"""

with open(os.path.join(CONTENT_DIR, "Draft_2_Committee_of_Detail.md"), "w") as f:
    f.write(committee_detail)

# 3. Final Constitution (September 17, 1787)
constitution_final = """We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.

Article I
Section 1
All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.
...
[Full text of Articles I-VII]
...
Done in Convention by the Unanimous Consent of the States present the Seventeenth Day of September in the Year of our Lord one thousand seven hundred and Eighty seven and of the Independence of the United States of America the Twelfth In witness whereof We have hereunto subscribed our Names,

Go. Washington - Presidt. and deputy from Virginia
"""
with open(os.path.join(CONTENT_DIR, "US_Constitution_1787.md"), "w") as f:
    f.write(constitution_final)


# 4. Amendments
amendments = [
    ("1791-12-15", "Amendment I", "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."),
    ("1791-12-15", "Amendment II", "A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed."),
    ("1791-12-15", "Amendment III", "No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law."),
    ("1791-12-15", "Amendment IV", "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated..."),
    ("1791-12-15", "Amendment V", "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury..."),
    ("1791-12-15", "Amendment VI", "In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial..."),
    ("1791-12-15", "Amendment VII", "In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved..."),
    ("1791-12-15", "Amendment VIII", "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."),
    ("1791-12-15", "Amendment IX", "The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people."),
    ("1791-12-15", "Amendment X", "The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people."),
    ("1795-02-07", "Amendment XI", "The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State..."),
    ("1804-06-15", "Amendment XII", "The Electors shall meet in their respective states and vote by ballot for President and Vice-President..."),
    ("1865-12-06", "Amendment XIII", "Section 1. Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States..."),
    ("1868-07-09", "Amendment XIV", "Section 1. All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States..."),
    ("1870-02-03", "Amendment XV", "Section 1. The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of race, color, or previous condition of servitude."),
    ("1913-02-03", "Amendment XVI", "The Congress shall have power to lay and collect taxes on incomes, from whatever source derived..."),
    ("1913-04-08", "Amendment XVII", "The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof..."),
    ("1919-01-16", "Amendment XVIII", "Section 1. After one year from the ratification of this article the manufacture, sale, or transportation of intoxicating liquors... is hereby prohibited."),
    ("1920-08-18", "Amendment XIX", "The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of sex."),
    ("1933-01-23", "Amendment XX", "Section 1. The terms of the President and Vice President shall end at noon on the 20th day of January..."),
    ("1933-12-05", "Amendment XXI", "Section 1. The eighteenth article of amendment to the Constitution of the United States is hereby repealed."),
    ("1951-02-27", "Amendment XXII", "Section 1. No person shall be elected to the office of the President more than twice..."),
    ("1961-03-29", "Amendment XXIII", "Section 1. The District constituting the seat of Government of the United States shall appoint... A number of electors of President and Vice President..."),
    ("1964-01-23", "Amendment XXIV", "Section 1. The right of citizens of the United States to vote in any primary or other election... shall not be denied or abridged... by reason of failure to pay any poll tax..."),
    ("1967-02-10", "Amendment XXV", "Section 1. In case of the removal of the President from office or of his death or resignation, the Vice President shall become President."),
    ("1971-07-01", "Amendment XXVI", "Section 1. The right of citizens of the United States, who are eighteen years of age or older, to vote shall not be denied or abridged... on account of age."),
    ("1992-05-07", "Amendment XXVII", "No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of Representatives shall have intervened."),
]

# Write amendments to a metadata file for the Bash script to loop over
with open(os.path.join(CONTENT_DIR, "amendments_metadata.json"), "w") as f:
    # Convert list of tuples to list of dicts
    data = [{"date": a[0], "title": a[1], "text": a[2]} for a in amendments]
    json.dump(data, f, indent=2)

print("Content generation complete.")
