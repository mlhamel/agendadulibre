# -*- encoding:utf-8 -*-
#
# Copyright (C) 2014 Mathieu Leduc-Hamel
#
# Author: Mathieu Leduc-Hamel <marrakis@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


def truncated_string(text, max_width=100):
    """ Return the truncated text to max_width """
    lo = 0
    hi = len(text)
    if hi <= max_width:
        return text
    while lo < hi:
        mid = (lo + hi) // 2
        if max_width < len(text[:mid]):
            hi = mid
        else:
            lo = mid + 1
    return text[:lo] + "..."
